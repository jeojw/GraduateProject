from env import OvercookedEnv
from agents import HumanAgent, AIAgent
from metrics import load_logs, compute_team_reward, compute_idle_time

env = OvercookedEnv(grid_size=(5,5))
human = HumanAgent('Human1')
ai = AIAgent('AI1')

env.add_agent('Human1','human',(0,0))
env.add_agent('AI1','ai',(4,4))

# 재료, 스토브, 배달 위치 배치 (예시)
env.place_object(3,(1,1)) # ingredient
env.place_object(2,(2,2)) # stove
env.place_object(4,(4,0)) # delivery

# 시뮬레이션
for step in range(20):
    actions = {
        'Human1': human.act(None),
        'AI1': ai.act(None)
    }
    env.step(actions)

# 로그 저장
env.save_logs()

# 지표 계산
logs = load_logs()
print("Team reward:", compute_team_reward(logs))
print("Idle time:", compute_idle_time(logs,['Human1','AI1']))