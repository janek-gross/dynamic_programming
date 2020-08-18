class Config(object):
    # Constants
    maze = None
    n_rows = None
    n_cols = None
    U = None # possible actions in each state
    delta = 1e-7 # used to check the value function for convergence
    vmin = -10 # plot parameters
    vmax = 10
    
    # valid entries in the maze file (free, start, trap, goal)
    valid_states = ['0', 'S', 'T', 'G'] # other entries are considered walls
    p = 0.1 # probability of going left or right instead of the intended action
    gamma = 0.9 # cost discount factor
    
    def display():
        for i in dir(Config):
            if not i.startswith("_") and not callable(getattr(Config, i)):
                print(i + ": " + str(getattr(Config, i)))
            
            
