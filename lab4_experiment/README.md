# AI + X: Lab 4 Experiments

***Team member: He Li, Haoyang Weng***

Before the following steps, please build the project by:

```bash
scons build/NULL/gem5.opt PROTOCOL=Garnet_standalone -j $(nproc)
```

## Verification of deadlock-free

We provide the following file to show that our implementation is deadlock-free. The bash file will simulate for 100000 cycles and the deadlock detection threshold is set to 5000. The result will be save to `./log.txt`.

```
./example.sh
```

## Topology Experiment

- All the result of **Topology** experiments can be reproduced with the code under the directory `lab4_experiment/code/topology`

- To reproduce the result of **\${n}-D \${k}-ary**, please find the subfolder `${n}d_${k}ary_torus`, you can follow the steps:

1. Make sure you are at the root directory `gem5`.
2. You need to make sure the following python packages are installed: `pandas`, `matplotlib`, `numpy`.
3. Run the bash script `./lab4_experiment/code/topology/${n}d_${k}ary_torus/experiment.sh` to run the simulation, the result will be saved in `lab4_experiment/log/topology`.
4. Run the python code `python ./lab4_experiment/code/topology/${n}d_${k}ary_torus/plot.py` to visualize the result, the images will be saved in `lab4_experiment/result/topology`.

- **TL;DR**

```bash
./lab4_experiment/code/topology/1d_64ary_torus/experiment.sh
python ./lab4_experiment/code/topology/1d_64ary_torus/plot.py

./lab4_experiment/code/topology/2d_8ary_torus/experiment.sh
python ./lab4_experiment/code/topology/2d_8ary_torus/plot.py

./lab4_experiment/code/topology/3d_4ary_torus/experiment.sh
python ./lab4_experiment/code/topology/3d_4ary_torus/plot.py
```

## Routing Algorithm Experiment

- All the result of **Routing** experiments can be reproduced with the code under the directory `lab4_experiment/code/routing`

- To reproduce the result, you can follow the steps:

1. Make sure you are at the root directory `gem5`.
2. You need to make sure the following python packages are installed: `pandas`, `matplotlib`, `numpy`.
3. Run the bash script `./lab4_experiment/code/routing/experiment.sh` to run the simulation, the result will be saved in `lab4_experiment/log/routing`.
4. Run the python code `python ./lab4_experiment/code/routing/plot.py` to visualize the result, the images will be saved in `lab4_experiment/result/routing`.

- **TL;DR**

```
./lab4_experiment/code/routing/experiment.sh
python ./lab4_experiment/code/routing/plot.py
```

## Random Quadrant Experiment

- All the result of **Quadrant** experiments can be reproduced with the code under the directory `lab4_experiment/code/quadrant`

- To reproduce the result, you can follow the steps:

1. Make sure you are at the root directory `gem5`.
2. You need to make sure the following python packages are installed: `pandas`, `matplotlib`, `numpy`.
3. Run the bash script `./lab4_experiment/code/quadrant/experiment.sh` to run the simulation, the result will be saved in `lab4_experiment/log/routing`.
4. Run the python code `python ./lab4_experiment/code/quadrant/plot.py` to visualize the result, the images will be saved in `lab4_experiment/result/routing`.

- **TL;DR**

```
./lab4_experiment/code/quadrant/experiment.sh
python ./lab4_experiment/code/quadrant/plot.py
```











