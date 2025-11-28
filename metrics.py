import pandas as pd
import json

def load_logs(path='logs/traj_logs.json'):
    with open(path) as f:
        return [json.loads(line) for line in f]

def compute_team_reward(logs):
    # 단순 예시: deliver 이벤트 1점
    return sum(1 for e in logs if e['action']=='deliver')

def compute_idle_time(logs, agent_names):
    last_time = max(e['time'] for e in logs)
    active_times = {name:0 for name in agent_names}
    for e in logs:
        if e['action'] not in ['up','down','left','right']:
            active_times[e['agent']] += 1
    idle_times = {name:last_time-active_times[name] for name in agent_names}
    return idle_times
