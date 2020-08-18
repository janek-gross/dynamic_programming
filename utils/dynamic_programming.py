import numpy as np
from utils.config import Config as c
from utils.maze_utilities import *

def expected_val(x, u, V, gamma, cost_fn):
    """
    Helper function that computes the expeced value for the bellman operator.
    """
    next_rows, next_cols, next_p = get_next_state(x,u)
    E = 0
    for i in range(len(next_p)):
        E+= next_p[i]*(cost_fn(x,[next_rows[i],next_cols[i]]) + gamma*V[next_rows[i],next_cols[i]])
    return E

def opt_bell(x, V, gamma, cost_fn):
    """
    Optimal Bellman operator evaluated in one state x.
    """
    allowed_actions = np.atleast_1d(np.argwhere(c.U[x[0],x[1],:]==1).squeeze())
    Es = []
    for u in allowed_actions:
        Es.append(expected_val(x,u, V, gamma, cost_fn))
    v_next = np.min(Es)
    return v_next

def bell(x, V, PI, gamma, cost_fn):
    """
    Bellman operator for policy PI evaluated in one state x.
    """
    u = PI[x[0],x[1]]
    v_next = expected_val(x,u,V, gamma, cost_fn)
    return v_next

def greedy_policy_improvement(x, V, gamma, cost_fn):
    """
    Computes the greedily induced policy for a given value function V in one state x.
    """
    allowed_actions = np.argwhere(c.U[x[0],x[1],:]==1)
    Es = []
    for u in allowed_actions:
        Es.append(expected_val(x, u, V, gamma, cost_fn))
    pi = allowed_actions[np.argmin(Es)]
    return pi


def value_iteration_step(V, gamma, cost_fn):
    """
    Computes one step of the value iteration for the value function V.
    """
    V_next = np.zeros_like(V)
    for i in range(1,c.n_rows-1):
        for j in range(1,c.n_cols-1):
            if c.maze[i,j] == '1':
                continue
            x = [i,j]
            V_next[i,j] = opt_bell(x, V, gamma, cost_fn)
    return V_next
                
def policy_evaluation_step(V, PI, gamma, cost_fn):
    """
    Computes one step of the policy evaluation for the value function V and the policy PI.
    """
    V_next = np.zeros_like(V)
    for i in range(1,c.n_rows-1):
        for j in range(1,c.n_cols-1):
            if c.maze[i,j] == '1':
                continue
            x = [i,j]
            V_next[i,j] = bell(x, V, PI, gamma, cost_fn)
    return V_next
            
def policy_improvement_step(V, gamma, cost_fn, PI):
    """
    Computes the greedily induced policy for a value function V
    """
    for i in range(1,c.n_rows-1):
        for j in range(1,c.n_cols-1):
            if c.maze[i,j] == '1':
                continue
            x = [i,j]
            PI[i,j] = greedy_policy_improvement(x, V, gamma, cost_fn)
    return PI

def test_converged(arg1, arg2):
    """
    Computes the maximum norm between arg1 and arg2 and
    checks whether the result is smaller than the global variable delta.
    """
    return np.max(np.abs(arg1-arg2)) < c.delta

def Value_Iteration(V, gamma, cost_fn):
    """
    Value iteration algorithm. Stops after convergence of max_steps.
    """
    max_steps = 1000000
    for i in range(max_steps):
        V_prev = V
        V = value_iteration_step(V, gamma, cost_fn)
        if test_converged(V, V_prev):
            return V
    else:
        print(f"failed to converge after {max_steps} steps.")

        
def Policy_Evaluation(V, PI, gamma, cost_fn, eval_steps = None):
    """
    Policy evaluation used for the policy iteration. It stops afer eval_step.
    If no value for eval_steps is given, Policy_Evaluation runs until
    convergence or until max_steps is reached.
    """
    if eval_steps != None:
        max_steps = eval_steps
    else:
        max_steps = 1000000
        
    if eval_steps != None:
        for i in range(max_steps):
            V_prev = V
            V = policy_evaluation_step(V, PI, gamma, cost_fn)
            if test_converged(V, V_prev):
                return V
        else: return V
        
    else:
        for i in range(max_steps):
            V_prev = V
            V = policy_evaluation_step(V, PI, gamma, cost_fn)
            if test_converged(V, V_prev):
                return V
        else:
            print(f"failed to converge after {max_steps} steps.")
    
def Policy_Iteration(V, PI, gamma, cost_fn, eval_steps = None):
    """
    This function computes the Policy_Iteration of no value for eval_steps is given.
    If eval_steps is given, it computes the optistic policy
    iteration with that many policy evaluation steps.
    """
    max_steps = 1000000
    for i in range(max_steps):
        V_prev = V
        V = Policy_Evaluation(V, PI, gamma, cost_fn, eval_steps)
        PI_prev = PI
        PI = policy_improvement_step(V, gamma, cost_fn, PI)
        if test_converged(V, V_prev):
            return PI, V
    else:
        print(f"failed to converge after {max_steps} steps.")

