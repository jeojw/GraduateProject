from metrics_baseline import *
from metrics_coop import compute_ccs
import json

def load_logs():
    with open("logs/traj.json") as f:
        return json.load(f)

def analyze_all():
    data = load_logs()
    steps = data["steps"]     # pos, time, agent, holding
    events = data["events"]   # time, agent, action, pos
    agents = ["Human1", "AI1"]

    print("\n===== Baseline Metrics =====")
    print("Idle Time:", compute_idle_time(steps, agents))
    print("Movement Distance:", compute_movement_distance(steps, agents))
    print("Collisions:", compute_collisions(steps))
    print("Rewards:", compute_team_reward(events))

    print("\n=== Cooperative Research Metric (CCS) ===")
    ccs = compute_ccs(steps)
    print("CCS:", ccs)

if __name__ == "__main__":
    analyze_all()

