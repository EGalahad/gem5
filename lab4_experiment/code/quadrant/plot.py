import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

log_dir="lab4_experiment/log/routing"
injection_rates = [round(x, 2) for x in np.arange(0.05, 1.0, 0.05)]
algorithms = [2, 3]
mapping = {2: "GOAL Routing", 3: "Dimension Order Routing"}

data = []

for rate in injection_rates:
    for algo in algorithms:
        result_file = os.path.join(log_dir, f"routing_algo_{algo}_injection_rate_{rate}.txt")
        if os.path.exists(result_file):
            with open(result_file, "r") as f:
                stats = {
                    line.split("(")[0]
                    .strip()
                    .split("=")[0]
                    .strip(): float(
                        line.split("(")[0].strip().split("=")[-1].strip()
                    )
                    for line in f.readlines()[2:]
                }
                stats["injection_rate"] = rate
                stats["algorithm"] = algo
                data.append(stats)

df = pd.DataFrame(data)

plt.figure(figsize=(10, 6))
for algo in algorithms:
    df_algo = df[df["algorithm"] == algo]
    plt.plot(df_algo["injection_rate"], df_algo["average_packet_latency"], label=f"Algorithm {mapping[algo]}")

plt.xlabel("Injection Rate")
plt.ylabel("Average Packet Latency")
plt.title("Latency-Throughput Curve for Shuffle Traffic")
plt.legend()
plt.grid(True)
plt.savefig(f"lab4_experiment/result/routing/routing_latency.png")

plt.figure(figsize=(10, 6))
for algo in algorithms:
    df_algo = df[df["algorithm"] == algo]
    plt.plot(df_algo["injection_rate"], df_algo["reception_rate"] * 2, label=f"Algorithm {mapping[algo]}")

plt.xlabel("Injection Rate")
plt.ylabel("Reception Rate")
plt.title("Latency-Throughput Curve for Shuffle Traffic")
plt.legend()
plt.grid(True)
plt.savefig(f"lab4_experiment/result/routing/routing_reception.png")


# Replace algorithm with mapping
df['algorithm'] = df['algorithm'].map(mapping)

analysis = (
    df.groupby("algorithm")
    .agg({"average_hops": ["mean", "std"]})
)

print(analysis)