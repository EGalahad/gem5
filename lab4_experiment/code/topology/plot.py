import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

log_dir="lab4_experiment/log/topology"
injection_rates = [round(x, 2) for x in np.arange(0.01, 1.0, 0.01)]

data = []

for rate in injection_rates:
    for k, n in [(64, 1), (8, 2), (4, 3)]: 
        result_file = os.path.join(log_dir, f"topology_kary_{k}_ndim_{n}_injection_rate_{rate}.txt")
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
                stats["n"] = n
                data.append(stats)

df = pd.DataFrame(data)

plt.figure(figsize=(10, 6))
for k, n in [(64, 1), (8, 2), (4, 3)]: 
    df_n = df[df["n"] == n]
    print(df_n)
    plt.plot(df_n["injection_rate"], df_n["average_packet_latency"], label=f"{n}-D {k}-ary Torus")

plt.xlim(0, 1)
plt.xlabel("Injection Rate")
plt.ylabel("Average Packet Latency")
plt.title("Topology Experiment: Latency to Injection Rate")
plt.legend()
plt.grid(True)
plt.savefig(f"lab4_experiment/result/topology/torus_latency.png")


plt.figure(figsize=(10, 6))
for k, n in [(64, 1), (8, 2), (4, 3)]: 
    df_n = df[df["n"] == n]
    plt.plot(df_n["injection_rate"], df_n["reception_rate"] * 2, label=f"{n}-D {k}-ary Torus")

plt.xlim(0, 1)
plt.xlabel("Injection Rate")
plt.ylabel("Reception Rate")
plt.title("Topology Experiment: Reception Rate to Injection Rate")
plt.legend()
plt.grid(True)
plt.savefig(f"lab4_experiment/result/topology/torus_reception.png")

print(df.agg({"average_hops": ["mean", "std"]}))