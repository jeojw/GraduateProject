import random

class HumanAgent:
    def __init__(self, name):
        self.name = name

    def act(self, obs):
        return random.choice(['up','down','left','right','pickup','drop','cook','deliver'])

class AIAgent:
    def __init__(self, name):
        self.name = name

    def act(self, obs):
        return 'right'