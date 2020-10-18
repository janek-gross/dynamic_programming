# dynamic_programming
This repository contains simple implementation of the popular dynamic programming algorithms Policy Iteration and Value Iteration. The algorithms are demonstrated on a simpe maze task. The agent receives rewards per step in the maze. State-transitions are subject to noise. This means that there is a small chance for the agent to move towards a different direction other then the chosen one. The algorithms compute the optimal actions for each cell.

# Requirements
- [x] Python 3
- [x] numpy
- [x] matplotlib

# Optimal Policies and Value Functions
The optimal policies are indicated by the arrows. These arrows show the optimal action in each cell. The state-value functions are indicated by the cell colors.
Currently the optimal policies and value functions for different cost functions g_1 and g_2 are shown. In this example the cost functions are the same as negative reward functions.

For both cost/reward functions the optimal policies are the same while the state-value functions are different.
<img src="https://github.com/janek-gross/dynamic_programming/blob/master/plots/cost: g1%20%20%20 Optimistic Policy Iteration.png?raw=true" width="600" />
<img src="https://github.com/janek-gross/dynamic_programming/blob/master/plots/cost: g2%20%20%20 Optimistic Policy Iteration.png?raw=true" width="600" />

# Usage
The maze can be specified in maze.txt. The maze has to be rectengular. Free space is indicated by 0 and walls are indicated by 1. S marks the starting location. G marks the goal and T are traps. Cost functions can be added or modified in utils/cost_functions.py. Examples are demonstrated in dynamic_programming.ipynb.

# License
https://unlicense.org


