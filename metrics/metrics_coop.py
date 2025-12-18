from collections import defaultdict

IMPORTANT = {"pickup", "drop", "cook", "deliver"}

def compute_ccs(events):
    timeline = defaultdict(list)

    for e in events:
        if e["action"] in IMPORTANT:
            timeline[e["time"]].append(e["agent"])

    if not timeline:
        return 0.0

    consistent = sum(
        1 for agents in timeline.values()
        if "Human1" in agents and "AI1" in agents
    )

    return consistent / len(timeline)
