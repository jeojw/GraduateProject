import numpy as np
import json
import os

class OvercookedEnv:
    def __init__(self, grid_size=(5,5)):
        self.grid_size = grid_size
        self.grid = np.zeros(grid_size, dtype=int)  # 0: empty, 1: counter, 2: stove, 3: ingredient, 4: delivery
        self.agents = {}
        self.time = 0
        self.logs = []

    def add_agent(self, agent_name, agent_type, pos):
        self.agents[agent_name] = {'type': agent_type, 'pos': pos, 'holding': None}

    def place_object(self, obj_type, pos):
        self.grid[pos] = obj_type

    def step(self, actions):
        """
        actions: dict {agent_name: action_string}
        action_string: 'up','down','left','right','pickup','drop','cook','deliver'
        """
        for name, action in actions.items():
            agent = self.agents[name]
            x, y = agent['pos']

            if action == 'up': new_pos = (max(x-1,0), y)
            elif action == 'down': new_pos = (min(x+1,self.grid_size[0]-1), y)
            elif action == 'left': new_pos = (x, max(y-1,0))
            elif action == 'right': new_pos = (x, min(y+1,self.grid_size[1]-1))
            else: new_pos = (x,y)

            agent['pos'] = new_pos

            # 이벤트 logging
            if action in ['pickup','drop','cook','deliver']:
                self.logs.append({'time':self.time,'agent':name,'action':action,'pos':new_pos,'holding':agent['holding']})

        self.time += 1

    def save_logs(self, path='logs/traj_logs.json'):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path,'w') as f:
            for entry in self.logs:
                f.write(json.dumps(entry)+'\n')