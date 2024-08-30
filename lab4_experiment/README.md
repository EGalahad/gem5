# AI + X: Lab 4 Experiments

***Team member: He Li, Haoyang Weng***

Before the following steps, please build the project by:

```bash
scons build/NULL/gem5.opt PROTOCOL=Garnet_standalone -j $(nproc)
```

## Verification of Deadlock-free

We provide the following file to show that our implementation is deadlock-free. The bash file will simulate for 100000 cycles and the deadlock detection threshold is set to 5000. The result will be save to `./log.txt`. Please make sure you are at the root directory `gem5`. Then you can run:

```bash
bash ./example.sh
```

## Original Experimental Data

- We have saved our experimental data in the folder `lab4_experiment/log`. If you trust our data, you can ignore the `*.sh` running commands and simply use the python code to reproduce our visualization results and table results.
- Notice: if you rerun the experiment, the original data will be replaced. Please restore them with the provided `git patch` file.

## Topology Experiment

- All the result of **Topology** experiments can be reproduced with the code under the directory `lab4_experiment/code/topology`

- To reproduce the result of **\${n}-D \${k}-ary**, please find the subfolder `${n}d_${k}ary_torus`, you can follow the steps:

1. Make sure you are at the root directory `gem5`.
2. You need to make sure the following python packages are installed: `pandas`, `matplotlib`, `numpy`.
3. Run the bash script `./lab4_experiment/code/topology/${n}d_${k}ary_torus/experiment.sh` to run the simulation, the result will be saved in `lab4_experiment/log/topology`.
4. Run the python code `python ./lab4_experiment/code/topology/${n}d_${k}ary_torus/plot.py` to visualize the result, the images will be saved in `lab4_experiment/result/topology`.

- To reproduce the results of all-in-one figure, you can refer to the python code at `./lab4_experiment/code/topology/plot.py`

- **TL;DR**

```bash
# 1-D 64-ary torus experiment
bash ./lab4_experiment/code/topology/1d_64ary_torus/experiment.sh
python ./lab4_experiment/code/topology/1d_64ary_torus/plot.py

# 2-D 8-ary torus experiment
bash ./lab4_experiment/code/topology/2d_8ary_torus/experiment.sh
python ./lab4_experiment/code/topology/2d_8ary_torus/plot.py

# 3-D 4-ary torus experiment
bash ./lab4_experiment/code/topology/3d_4ary_torus/experiment.sh
python ./lab4_experiment/code/topology/3d_4ary_torus/plot.py

# Plot all topologies experimental results
python ./lab4_experiment/code/topology/plot.py
```

## Routing Algorithm Experiment

- All the result of **Routing** experiments can be reproduced with the code under the directory `lab4_experiment/code/routing`

- To reproduce the result, you can follow the steps:

1. Make sure you are at the root directory `gem5`.
2. You need to make sure the following python packages are installed: `pandas`, `matplotlib`, `numpy`.
3. Run the bash script `./lab4_experiment/code/routing/experiment.sh` to run the simulation, the result will be saved in `lab4_experiment/log/routing`.
4. Run the python code `python ./lab4_experiment/code/routing/plot.py` to visualize the result, the images will be saved in `lab4_experiment/result/routing`.

- **TL;DR**

```bash
# Routing experiment
bash ./lab4_experiment/code/routing/experiment.sh
python ./lab4_experiment/code/routing/plot.py
```

## Random Quadrant Experiment

- All the result of **Quadrant** experiments can be reproduced with the code under the directory `lab4_experiment/code/quadrant`

- To reproduce the result, you can follow the steps:

1. Make sure you are at the root directory `gem5`.
2. You need to make sure the following python packages are installed: `pandas`, `matplotlib`, `numpy`.
3. Run the bash script `./lab4_experiment/code/quadrant/experiment.sh` to run the simulation, the result will be saved in `lab4_experiment/log/quadrant`.
4. Run the python code `python ./lab4_experiment/code/quadrant/plot.py` to visualize the result, the images will be saved in `lab4_experiment/result/quadrant`.

- **TL;DR**

```bash
# Quadrant experiment
bash ./lab4_experiment/code/quadrant/experiment.sh
python ./lab4_experiment/code/quadrant/plot.py
```











