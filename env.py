import numpy as np
import json

class OvercookedEnv:
    def __init__(self, grid_size=(5,5)):
        self.grid_size = grid_size
        self.grid = np.zeros(grid_size, dtype=int)
        self.agents = {}
        self.time = 0

        # 오브젝트 위치
        self.objects = {
            "ingredient": None,
            "stove": None,
            "delivery": None
        }

    # ----------------------------------------------------
    # 에이전트 추가 및 참조 연결
    # ----------------------------------------------------
    def add_agent(self, agent_name, agent_type, pos):
        self.agents[agent_name] = {
            "type": agent_type,
            "pos": pos,
            "holding": None,
            "ref": None
        }

    def register_agent_instance(self, name, instance):
        self.agents[name]["ref"] = instance

    # ----------------------------------------------------
    # 오브젝트 배치
    # ----------------------------------------------------
    def place_object(self, obj_type, pos):
        self.grid[pos] = obj_type
        
        if obj_type == 3:
            self.objects["ingredient"] = pos
        elif obj_type == 2:
            self.objects["stove"] = pos
        elif obj_type == 4:
            self.objects["delivery"] = pos

    # ----------------------------------------------------
    # Observation 생성
    # ----------------------------------------------------
    def build_obs(self, agent_name):
        agent = self.agents[agent_name]
        return {
            "self_pos": agent["pos"],
            "holding": agent["holding"],
            "ingredient": self.objects["ingredient"],
            "stove": self.objects["stove"],
            "delivery": self.objects["delivery"]
        }

    # ----------------------------------------------------
    # 한 스텝 실행
    # ----------------------------------------------------
    def step(self):
        actions = {}
        
        # 1) obs 기반으로 각 에이전트의 행동 결정
        for name in self.agents:
            obs = self.build_obs(name)
            act = self.agents[name]["ref"].act(obs)
            actions[name] = act

        events = []

        # 2) 행동 실행
        for name, action in actions.items():
            agent = self.agents[name]
            x, y = agent["pos"]

            # 이동 처리
            if action == "up":
                new_pos = (max(x-1,0), y)
            elif action == "down":
                new_pos = (min(x+1,self.grid_size[0]-1), y)
            elif action == "left":
                new_pos = (x, max(y-1,0))
            elif action == "right":
                new_pos = (x, min(y+1,self.grid_size[1]-1))
            else:
                new_pos = (x, y)

            agent["pos"] = new_pos

            # 상호작용 처리
            obj = self.grid[new_pos]

            if action == "pickup":
                if obj == 3 and agent["holding"] is None:
                    agent["holding"] = "ingredient"
                    events.append({"time": self.time, "agent": name, "action": "pickup", "pos": new_pos})

            elif action == "drop":
                if agent["holding"] is not None:
                    agent["holding"] = None
                    events.append({"time": self.time, "agent": name, "action": "drop", "pos": new_pos})

            elif action == "cook":
                if obj == 2 and agent["holding"] == "ingredient":
                    agent["holding"] = "cooked"
                    events.append({"time": self.time, "agent": name, "action": "cook", "pos": new_pos})

            elif action == "deliver":
                if obj == 4 and agent["holding"] == "cooked":
                    agent["holding"] = None
                    events.append({"time": self.time, "agent": name, "action": "deliver", "pos": new_pos})

        # 3) 상태 반환
        agent_states = {
            name: {
                "pos": a["pos"],
                "holding": a["holding"]
            }
            for name, a in self.agents.items()
        }

        self.time += 1
        return agent_states, events, actions