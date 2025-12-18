import numpy as np
from scipy.stats import ttest_ind

def compare_variance(metric_a, metric_b):
    var_a = np.var(metric_a)
    var_b = np.var(metric_b)
    t_stat, p_value = ttest_ind(metric_a, metric_b)
    return var_a, var_b, t_stat, p_value