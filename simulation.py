import json, os
from env import OvercookedEnv
from agents import HumanAgent, AIAgent

# ----------------------
# 환경 초기화
# ----------------------
env = OvercookedEnv(grid_size=(5,5))

human = HumanAgent("Human1")
ai = AIAgent("AI1")

# 에이전트 등록
env.add_agent("Human1", "human", (0,0))
env.add_agent("AI1", "ai", (4,4))

# agent instance 연결 (obs 전달용)
env.register_agent_instance("Human1", human)
env.register_agent_instance("AI1", ai)

# 오브젝트 배치
env.place_object(3,(1,1))   # ingredient
env.place_object(2,(2,2))   # stove
env.place_object(4,(4,0))   # delivery

# 로그 구조
log = {
    "steps": [],
    "events": []
}

# ----------------------
# 시뮬레이션 루프
# ----------------------
for t in range(20):

    # env.step()에서 actions까지 함께 반환되도록 설계됨
    agent_states, events, actions = env.step()

    # step 로그 기록
    for agent in agent_states:
        log["steps"].append({
            "time": env.time,
            "agent": agent,
            "pos": agent_states[agent]["pos"],
            "holding": agent_states[agent]["holding"],
            "action": actions[agent]
        })

    # event 기록
    for e in events:
        log["events"].append(e)

# ----------------------
# JSON 저장
# ----------------------
os.makedirs("logs", exist_ok=True)
with open("logs/traj.json", "w") as f:
    json.dump(log, f, indent=2)

print("로그 저장 완료: logs/traj.json")
