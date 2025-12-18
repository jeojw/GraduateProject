import matplotlib.pyplot as plt

def plot_metrics(df):
    plt.figure(figsize=(10,5))
    plt.plot(df["episode"], df["TeamReward"], label="Team Reward")
    plt.plot(df["episode"], df["ActionAlignment"], label="Action Alignment")
    plt.plot(df["episode"], df["CCS"], label="CCS", linewidth=3)
    plt.legend()
    plt.xlabel("Episode")
    plt.ylabel("Metric Value")
    plt.title("Comparison of Collaboration Metrics")
    plt.grid(True)
    plt.show()