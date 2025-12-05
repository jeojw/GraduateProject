from collections import defaultdict

def compute_idle_time(steps, agents):
    idle = {a: 0 for a in agents}
    for s in steps:
        if s["action"] == "idle":
            idle[s["agent"]] += 1
    return idle

def compute_movement_distance(steps, agents):
    prev = {}
    dist = {a: 0 for a in agents}

    for s in steps:
        a = s["agent"]
        pos = tuple(s["pos"])
        if a in prev:
            (x1,y1) = prev[a]
            (x2,y2) = pos
            dist[a] += abs(x1-x2) + abs(y1-y2)
        prev[a] = pos
    return dist

def compute_collisions(steps):
    time_map = defaultdict(list)
    for s in steps:
        time_map[s["time"]].append(tuple(s["pos"]))

    collisions = 0
    for poses in time_map.values():
        if len(poses) != len(set(poses)):
            collisions += 1
    return collisions

def compute_team_reward(events):
    return sum(1 for e in events if e["action"] == "deliver")
