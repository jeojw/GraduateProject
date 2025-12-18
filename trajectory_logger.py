class TrajectoryLogger:
    def __init__(self):
        self.events = []

    def log(self, t, agent, action, state, reward):
        self.events.append({
            "time": t,
            "agent": agent,
            "action": action,
            "reward": reward,
            "held_object": str(state.players[0].held_object),
            "pos": state.players[0].position
        })

    def get_events(self):
        return self.events