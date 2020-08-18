import numpy as np
from utils.config import Config as c

def readmaze(filename):
    """
    This function reads the maze which is saved under filename.
    """
    file = open(filename)
    text = file.readlines()
    list(map(str.strip, text))
    c.maze = []
    for line in text:
        if line[0] != "#":
            c.maze.append(line.split())
    return np.array(c.maze)

def get_allowed_actions():
    """
    This function computes the allowed actions u in each state.
    Actions are encoded by integer values
    idle  up  down left right
    0    1    2    3    4
    """
    U = np.zeros((c.n_rows, c.n_cols, 5))
    for i in range(c.n_rows):
        for j in range(c.n_cols):
            if c.maze[i,j] in c.valid_states:
                U[i,j,0] = 1 # idling
                if c.maze[i,j] != 'G':
                    if c.maze[i-1,j] in c.valid_states:
                        U[i,j,1] = 1 # up

                    if c.maze[i+1,j] in c.valid_states:
                        U[i,j,2] = 1 # down

                    if c.maze[i,j-1] in c.valid_states:
                        U[i,j,3] = 1 # left

                    if c.maze[i,j+1] in c.valid_states:
                        U[i,j,4] = 1 # right
    return U

def get_next_state(x, u):
    """
    This function returns a list of column indices,
    row indices and probabilities of all possible next states
    for state x and action u.
    """
    next_rows = []
    next_cols = []
    next_p = []
    if u == 0:
        next_rows.append(x[0])
        next_cols.append(x[1])
        next_p.append(1)
        return next_rows, next_cols, next_p
    elif u == 1:
        next_rows.append(x[0]-1)
        next_cols.append(x[1])
        next_p.append(1-2*c.p)
        if c.maze[x[0]-1,x[1]-1] in c.valid_states:
            next_rows.append(x[0]-1)
            next_cols.append(x[1]-1)
            next_p.append(c.p)
        else:
            next_p[0] += c.p
            
        if c.maze[x[0]-1,x[1]+1] in c.valid_states:
            next_rows.append(x[0]-1)
            next_cols.append(x[1]+1)
            next_p.append(c.p)
        else:
            next_p[0] += c.p
        return next_rows, next_cols, next_p
    elif u == 2:
        next_rows.append(x[0]+1)
        next_cols.append(x[1])
        next_p.append(1-2*c.p)
        if c.maze[x[0]+1,x[1]-1] in c.valid_states:
            next_rows.append(x[0]+1)
            next_cols.append(x[1]-1)
            next_p.append(c.p)
        else:
            next_p[0] += c.p
            
        if c.maze[x[0]+1,x[1]+1] in c.valid_states:
            next_rows.append(x[0]+1)
            next_cols.append(x[1]+1)
            next_p.append(c.p)
        else:
            next_p[0] += c.p
        return next_rows, next_cols, next_p
    elif u == 3:
        next_rows.append(x[0])
        next_cols.append(x[1]-1)
        next_p.append(1-2*c.p)
        if c.maze[x[0]-1,x[1]-1] in c.valid_states:
            next_rows.append(x[0]-1)
            next_cols.append(x[1]-1)
            next_p.append(c.p)
        else:
            next_p[0] += c.p
            
        if c.maze[x[0]+1,x[1]-1] in c.valid_states:
            next_rows.append(x[0]+1)
            next_cols.append(x[1]-1)
            next_p.append(c.p)
        else:
            next_p[0] += c.p
        return next_rows, next_cols, next_p
    elif u == 4:
        next_rows.append(x[0])
        next_cols.append(x[1]+1)
        next_p.append(1-2*c.p)
        if c.maze[x[0]-1,x[1]+1] in c.valid_states:
            next_rows.append(x[0]-1)
            next_cols.append(x[1]+1)
            next_p.append(c.p)
        else:
            next_p[0] += c.p
            
        if c.maze[x[0]+1,x[1]+1] in c.valid_states:
            next_rows.append(x[0]+1)
            next_cols.append(x[1]+1)
            next_p.append(c.p)
        else:
            next_p[0] += c.p
        return next_rows, next_cols, next_p
    else:
        print(type(u),u)
        assert()
        
        