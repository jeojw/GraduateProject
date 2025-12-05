import json
import matplotlib.pyplot as plt
from metrics_baseline import *
from metrics_coop import compute_ccs

def load_logs():
    with open("logs/traj.json") as f:
        return json.load(f)

def plot_baseline_vs_ccs():
    data = load_logs()
    steps = data["steps"]
    events = data["events"]
    agents = ["Human1","AI1"]

    idle = compute_idle_time(steps, agents)
    move = compute_movement_distance(steps, agents)
    coll = compute_collisions(steps)
    reward = compute_team_reward(events)
    ccs = compute_ccs(events)

    baseline_scores = [sum(idle.values()), sum(move.values()), coll, reward]
    labels = ["Idle Time", "Movement", "Collisions", "Reward"]

    plt.figure(figsize=(8,5))
    plt.bar(labels, baseline_scores, alpha=0.6, label="Baseline Metrics")
    plt.axhline(ccs, color='red', linestyle="--", label=f"CCS={ccs:.2f}")
    plt.title("Baseline Metrics vs CCS")
    plt.legend()
    plt.ylabel("Scores")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_baseline_vs_ccs()
