from metrics.metrics_coop import compute_ccs
from metrics.metrics_baseline import team_reward, action_alignment

def compute_all_metrics(events):
    return {
        "TeamReward": team_reward(events),
        "ActionAlignment": action_alignment(events),
        "CCS": compute_ccs(events)
    }