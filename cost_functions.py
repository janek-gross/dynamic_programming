from utils.config import Config as c

def g_1(x,x_next):
    """
    First cost function.
    """
    cost = 0
    if c.maze[x_next[0],x_next[1]] == 'G':
        cost = -1
    if c.maze[x_next[0],x_next[1]] == 'T':
        cost += 40
    return cost

def g_2(x,x_next):
    """
    Alternative cost function.
    """
    cost = 1
    if c.maze[x_next[0],x_next[1]] == 'G':
        cost = 0
    if c.maze[x_next[0],x_next[1]] == 'T':
        cost += 20
    return cost