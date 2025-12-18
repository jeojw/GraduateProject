import pandas as pd
from env import OvercookedEnvWrapper
from agents import HumanAgent
from agents import StrategicRuleAgent
from rollout_runner import run_episode
from metrics.metric_runner import compute_all_metrics
from analysis.visualize import plot_metrics
from analysis.statistical_test import compare_variance

env = OvercookedEnvWrapper("cramped_room")
human = HumanAgent()
ai = StrategicRuleAgent()

results = []

for ep in range(30):
    events = run_episode(env, human, ai)
    metrics = compute_all_metrics(events)
    metrics["episode"] = ep
    results.append(metrics)

df = pd.DataFrame(results)
plot_metrics(df)

var_r, var_c, t, p = compare_variance(df["TeamReward"], df["CCS"])
print("Reward variance:", var_r)
print("CCS variance:", var_c)
print("t-test p-value:", p)