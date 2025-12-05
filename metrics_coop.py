# metrics_coop.py
from collections import defaultdict

IMPORTANT = {"pickup", "drop", "cook", "deliver"}

def compute_ccs(events):
    timeline = defaultdict(list)

    for e in events:
        if e["action"] in IMPORTANT:
            timeline[e["time"]].append(e["agent"])

    if not timeline:
        return 0

    consistent = 0
    for t, agents in timeline.items():
        if "Human1" in agents and "AI1" in agents:
            consistent += 1

    return consistent / len(timeline)
