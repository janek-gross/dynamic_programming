# dynamic_programming
This repository contains simple implementation of the popular dynamic programming algorithms policy iteration and value iteration. The algorithms are demonstrated on a simpe maze task. The agent receives different rewards per step in the maze. State-transitions are subject to noise. The algorithms compute the optimal actions for each cell.

# Requirements
- [x] Python 3
- [x] numpy
- [x] matplotlib

# Optimal Policies
The optimal policies for different cost functions g_1 and g_2 are usually the same.
The maze can be specified in maze.txt. S marks the starting location. G marks the goal and T are traps. Arrows indicate the optimal action for each cell.


<img src="https://github.com/janek-gross/dynamic_programming/blob/master/plots/cost: g1%20%20%20 Optimistic Policy Iteration.png?raw=true" width="600" />
<img src="https://github.com/janek-gross/dynamic_programming/blob/master/plots/cost: g2%20%20%20 Optimistic Policy Iteration.png?raw=true" width="600" />



