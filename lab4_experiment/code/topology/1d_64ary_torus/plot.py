import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

log_dir="lab4_experiment/log/topology"
k = 64
n = 1
injection_rates = [round(x, 2) for x in np.arange(0.01, 0.2, 0.01)]

data = []

for rate in injection_rates:
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
            data.append(stats)

df = pd.DataFrame(data)

plt.figure(figsize=(10, 6))
plt.plot(df["injection_rate"], df["average_packet_latency"], label=f"{n}-D {k}-ary Torus")

plt.xlabel("Injection Rate")
plt.ylabel("Average Packet Latency")
plt.title("Latency-Throughput Curve for Uniform Random Traffic")
plt.legend()
plt.grid(True)
plt.savefig(f"lab4_experiment/result/topology/{n}d_{k}ary_torus_latency.png")

plt.figure(figsize=(10, 6))
plt.plot(df["injection_rate"], df["reception_rate"] * 2, label=f"{n}-D {k}-ary Torus")

plt.xlabel("Injection Rate")
plt.ylabel("Reception Rate")
plt.title("Latency-Throughput Curve for Uniform Random Traffic")
plt.legend()
plt.grid(True)
plt.savefig(f"lab4_experiment/result/topology/{n}d_{k}ary_torus_reception.png")

print(df.agg({"average_hops": ["mean", "std"]}))