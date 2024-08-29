# Deadlock-free Verifier
FLOW_CONTROL=1
KARY=4
NDIM=3
SYNTHETIC=uniform_random
ALGORITHM=2
N_CORES=$(( $KARY ** $NDIM ))
echo "kary = $KARY, ndim = $NDIM, ncores = $N_CORES"

./build/NULL/gem5.opt \
configs/example/garnet_synth_traffic.py --network=garnet --num-cpus=$N_CORES --num-dirs=$N_CORES --topology=Torus --kary=$KARY --ndim=$NDIM --routing-algorithm=$ALGORITHM --inj-vnet=0 --synthetic=$SYNTHETIC --injectionrate=1 --sim-cycles=200000 --garnet-deadlock-threshold 5000 --flow-control $FLOW_CONTROL --randomize_quadrant

result_file=log.txt
echo > $result_file
grep "packets_injected::total" m5out/stats.txt | sed 's/system.ruby.network.packets_injected::total\s*/packets_injected = /' >> $result_file
grep "packets_received::total" m5out/stats.txt | sed 's/system.ruby.network.packets_received::total\s*/packets_received = /' >> $result_file
grep "average_packet_queueing_latency" m5out/stats.txt | sed 's/system.ruby.network.average_packet_queueing_latency\s*/average_packet_queueing_latency = /' >> $result_file
grep "average_packet_network_latency" m5out/stats.txt | sed 's/system.ruby.network.average_packet_network_latency\s*/average_packet_network_latency = /' >> $result_file
grep "average_packet_latency" m5out/stats.txt | sed 's/system.ruby.network.average_packet_latency\s*/average_packet_latency = /' >> $result_file
grep "average_hops" m5out/stats.txt | sed 's/system.ruby.network.average_hops\s*/average_hops = /' >> $result_file
grep "reception_rate" m5out/stats.txt | sed 's/system.ruby.network.reception_rate\s*/reception_rate = /' >> $result_file
