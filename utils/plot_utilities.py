import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from utils.config import Config as c

def plot_result(V, PI, title = None):
    """
    This function plots the maze value function V and policy PI.
    """
    norm = mpl.colors.Normalize(vmin = c.vmin, vmax = c.vmax)
    normed_V = norm(V)
    cmap = plt.get_cmap('jet')
    colors = cmap(normed_V)
    
    fig,ax = plt.subplots(1, figsize= (c.n_cols+2,c.n_rows))
    for i in range(c.n_rows):
        for j in range(c.n_cols):
            if c.maze[i,j] == '1':
                ax.add_patch(patches.Rectangle((j,c.n_rows-i-1),1,1,linewidth=1,edgecolor='black',facecolor='black'))
            else:
                ax.add_patch(patches.Rectangle((j,c.n_rows-i-1),1,1,linewidth=1,edgecolor='black',facecolor=colors[i,j,:]))
                u = PI[i,j]
                if u == 0:
                    dx = 0
                    dy = 0
                elif u == 1:
                    dx = 0
                    dy = .4
                elif u == 2:
                    dx = 0
                    dy = -.4
                elif u == 3:
                    dx = -.4
                    dy = 0
                elif u == 4:
                    dx = .4
                    dy = 0

                ax.arrow(j+0.5, c.n_rows-i-1+0.5, dx, dy, width = .02, head_width = .1, head_length=0.1, fc='k', ec='k')
                if c.maze[i,j] != '0':
                    ax.text(j+0.1, c.n_rows-i-1+0.1, c.maze[i,j], color= "white", fontsize = 20, fontweight = "bold")
                    
    ax.set_xlim(0, c.n_cols)
    ax.set_ylim(0, c.n_rows)
    sm = mpl.cm.ScalarMappable(norm=norm, cmap=cmap)
    sm._A = []
    fig.colorbar(mappable = sm, ax=ax)
    ax.set_title(title, fontsize = 30)
    #plt.savefig(title,bbox_inches = 'tight', pad_inches = 0)
    plt.show()