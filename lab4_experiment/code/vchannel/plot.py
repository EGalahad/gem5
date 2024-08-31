import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

log_dir="lab4_experiment/log/vchannel"
injection_rates = [round(x, 2) for x in np.arange(0.05, 1.0, 0.05)]
vchannels = [3, 6, 9]

data = []

for rate in injection_rates:
    for vchannel in vchannels:
        result_file = os.path.join(log_dir, f"quadrant_injection_rate_{rate}_vcs_{vchannel}.txt")
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
                stats["vchannel"] = vchannel
                data.append(stats)

df = pd.DataFrame(data)

plt.figure(figsize=(10, 6))
for vchannel in vchannels:
    df_vcs = df[df["vchannel"] == vchannel]
    plt.plot(df_vcs["injection_rate"], df_vcs["average_packet_latency"], label=f"{vchannel} Virtual Channels")

plt.xlabel("Injection Rate")
plt.ylabel("Average Packet Latency")
plt.title("Virtual Channel Experiment: Latency to Injection Rate")
plt.legend()
plt.grid(True)
plt.savefig(f"lab4_experiment/result/vchannel/vchannel_latency.png")

plt.figure(figsize=(10, 6))
for vchannel in vchannels:
    df_vcs = df[df["vchannel"] == vchannel]
    plt.plot(df_vcs["injection_rate"], df_vcs["reception_rate"] * 2, label=f"{vchannel} Virtual Channels")

plt.xlabel("Injection Rate")
plt.ylabel("Reception Rate")
plt.title("Virtual Channel Experiment: Reception Rate to Injection Rate")
plt.legend()
plt.grid(True)
plt.savefig(f"lab4_experiment/result/vchannel/vchannel_reception.png")


analysis = (
    df.groupby(["vchannel"])
    .agg({"average_hops": ["mean", "std"]})
)

print(analysis)