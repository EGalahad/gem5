# Description: This script is used to run the experiment for the topology of the network.

log_dir=lab4_experiment/log/topology
mkdir -p $log_dir

KARY=8
NDIM=2
SYNTHETIC=uniform_random
N_CORES=$(( $KARY ** $NDIM ))
injection_rates=$(seq 0.05 0.05 1.0)

for rate in $injection_rates; do
    # Run the experiment
    ./build/NULL/gem5.opt \
    configs/example/garnet_synth_traffic.py \
    --network=garnet --num-cpus=$N_CORES --num-dirs=$N_CORES \
    --topology=Torus --kary=$KARY --ndim=$NDIM \
    --routing-algorithm=2 \
    --inj-vnet=0 --synthetic=$SYNTHETIC \
    --injectionrate=$rate \
    --sim-cycles=10000 \
    --garnet-deadlock-threshold 10000 \
    --flow-control 1 \
    --randomize_quadrant

    # Save the results
    result_file=$log_dir/topology_kary_${KARY}_ndim_${NDIM}_injection_rate_${rate}.txt
    echo > $result_file
    grep "packets_injected::total" m5out/stats.txt | sed 's/system.ruby.network.packets_injected::total\s*/packets_injected = /' >> $result_file
    grep "packets_received::total" m5out/stats.txt | sed 's/system.ruby.network.packets_received::total\s*/packets_received = /' >> $result_file
    grep "average_packet_queueing_latency" m5out/stats.txt | sed 's/system.ruby.network.average_packet_queueing_latency\s*/average_packet_queueing_latency = /' >> $result_file
    grep "average_packet_network_latency" m5out/stats.txt | sed 's/system.ruby.network.average_packet_network_latency\s*/average_packet_network_latency = /' >> $result_file
    grep "average_packet_latency" m5out/stats.txt | sed 's/system.ruby.network.average_packet_latency\s*/average_packet_latency = /' >> $result_file
    grep "average_hops" m5out/stats.txt | sed 's/system.ruby.network.average_hops\s*/average_hops = /' >> $result_file
    grep "reception_rate" m5out/stats.txt | sed 's/system.ruby.network.reception_rate\s*/reception_rate = /' >> $result_file
done