import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

log_dir="lab4_experiment/log/quadrant"
injection_rates = [round(x, 2) for x in np.arange(0.05, 1.0, 0.05)]
traffics = ["uniform_random", "shuffle"]

data = []

for rate in injection_rates:
    for traffic in traffics:
        result_file = os.path.join(log_dir, f"quadrant_synthetic_{traffic}_injection_rate_{rate}_derandom.txt")
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
                stats["traffic"] = traffic
                stats["quadrant"] = "derandom"
                data.append(stats)
        result_file = os.path.join(log_dir, f"quadrant_synthetic_{traffic}_injection_rate_{rate}_random.txt")
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
                stats["traffic"] = traffic
                stats["quadrant"] = "random"
                data.append(stats)

df = pd.DataFrame(data)

plt.figure(figsize=(10, 6))
for traffic in traffics:
    df_traffic = df[df["traffic"] == traffic]
    for quadrant in ["derandom", "random"]:
        df_quadrant = df_traffic[df_traffic["quadrant"] == quadrant]
        plt.plot(df_quadrant["injection_rate"], df_quadrant["average_packet_latency"], label=f"{traffic} Traffic {quadrant} Quadrant")

plt.xlabel("Injection Rate")
plt.ylabel("Average Packet Latency")
plt.title("Latency-Throughput Curve for Different Traffic")
plt.legend()
plt.grid(True)
plt.savefig(f"lab4_experiment/result/quadrant/quadrant_latency.png")

plt.figure(figsize=(10, 6))
for traffic in traffics:
    df_traffic = df[df["traffic"] == traffic]
    for quadrant in ["derandom", "random"]:
        df_quadrant = df_traffic[df_traffic["quadrant"] == quadrant]
        plt.plot(df_quadrant["injection_rate"], df_quadrant["reception_rate"] * 2, label=f"{traffic} Traffic {quadrant} Quadrant")

plt.xlabel("Injection Rate")
plt.ylabel("Reception Rate")
plt.title("Latency-Throughput Curve for Different Traffic")
plt.legend()
plt.grid(True)
plt.savefig(f"lab4_experiment/result/quadrant/quadrant_reception.png")


analysis = (
    df.groupby(["traffic", "quadrant"])
    .agg({"average_hops": ["mean", "std"]})
)

print(analysis)