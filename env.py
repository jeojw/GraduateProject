from overcooked_ai_py.mdp.overcooked_mdp import OvercookedGridworld
from overcooked_ai_py.mdp.overcooked_env import OvercookedEnv

class OvercookedEnvWrapper:
    def __init__(self, layout_name, horizon=400):
        mdp = OvercookedGridworld.from_layout_name(layout_name)
        self.env = OvercookedEnv.from_mdp(mdp, horizon=horizon)

    def reset(self):
        return self.env.reset()

    def step(self, joint_action):
        return self.env.step(joint_action)