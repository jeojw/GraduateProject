import random

def move_towards(curr, target):
    cx, cy = curr
    tx, ty = target

    if cx < tx: return "down"
    if cx > tx: return "up"
    if cy < ty: return "right"
    if cy > ty: return "left"
    return "idle"


class HumanAgent:
    def __init__(self, name):
        self.name = name
        self.state = "pickup"   # pickup → move_to_stove → cook → idle

    def act(self, obs):
        human_pos = obs["self_pos"]
        ingredient_pos = obs["ingredient"]
        stove_pos = obs["stove"]

        if ingredient_pos is None or stove_pos is None:
            return "idle"

        # --- 상태 기반 행동 ---
        if self.state == "pickup":
            if human_pos == ingredient_pos:
                self.state = "move_to_stove"
                return "pickup"
            return move_towards(human_pos, ingredient_pos)

        elif self.state == "move_to_stove":
            if human_pos == stove_pos:
                self.state = "cook"
                return "drop"
            return move_towards(human_pos, stove_pos)

        elif self.state == "cook":
            self.state = "idle"
            return "cook"

        return random.choice(["up", "down", "left", "right"])


class AIAgent:
    def __init__(self, name):
        self.name = name
        self.state = "wait"  
        # wait → move_to_stove → pickup_food → move_to_delivery → deliver → idle

    def act(self, obs):
        ai_pos = obs["self_pos"]
        stove_pos = obs["stove"]
        delivery_pos = obs["delivery"]

        if stove_pos is None or delivery_pos is None:
            return "idle"

        if self.state == "wait":
            self.state = "move_to_stove"
            return "idle"

        elif self.state == "move_to_stove":
            if ai_pos == stove_pos:
                self.state = "pickup_food"
                return "pickup"
            return move_towards(ai_pos, stove_pos)

        elif self.state == "pickup_food":
            self.state = "move_to_delivery"
            return "pickup"

        elif self.state == "move_to_delivery":
            if ai_pos == delivery_pos:
                self.state = "deliver"
                return "deliver"
            return move_towards(ai_pos, delivery_pos)

        elif self.state == "deliver":
            self.state = "idle"
            return "deliver"

        return "idle"
