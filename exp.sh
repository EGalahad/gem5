KARY=4
NDIM=3
# ncores = kary^ndim
N_CORES=$(( $KARY ** $NDIM ))
echo "kary = $KARY, ndim = $NDIM, ncores = $N_CORES"

./build/NULL/gem5.opt \
configs/example/garnet_synth_traffic.py \
--network=garnet --num-cpus=$N_CORES --num-dirs=$N_CORES \
--topology=Torus --kary=$KARY --ndim=$NDIM \
--routing-algorithm=2 \
--inj-vnet=0 --synthetic=uniform_random \
--injectionrate=0.01 \
--sim-cycles=50000 \
--garnet-deadlock-threshold 10000 \
--flow-control 0 \
