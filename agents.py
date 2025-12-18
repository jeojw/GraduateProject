class BaseAgent:
    def __init__(self, name):
        self.name = name

    def act(self, obs):
        raise NotImplementedError

    def observe(self, obs):
        pass

class HumanAgent(BaseAgent):
    def __init__(self, name="Human1"):
        super().__init__(name)
        self.current_intent = None

    def infer_intent(self, state):
        if state.players[0].held_object is None:
            return "pickup"
        return "deliver"

    def act(self, obs):
        state = obs["state"]
        self.current_intent = self.infer_intent(state)

        if self.current_intent == "pickup":
            return "pickup"
        elif self.current_intent == "deliver":
            return "deliver"
        return "stay"

class StrategicRuleAgent(BaseAgent):
    def __init__(self, name="AI1"):
        super().__init__(name)
        self.role = None

    def assign_role(self, state):
        if state.players[1].held_object is None:
            self.role = "collector"
        else:
            self.role = "deliverer"

    def act(self, obs):
        state = obs["state"]
        self.assign_role(state)

        if self.role == "collector":
            return "pickup"
        elif self.role == "deliverer":
            return "deliver"
        return "stay"
