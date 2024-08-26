import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
# let's say mr x arrives at time x, and mr y arrives at time y. We want to know the probability of
# x and y arriving at a z distance in time. If z==0, x and y arrive at the same time. If z==1 (z is
# upper bounded at 1, since they can only arrive with one hour of difference), they arrive with 1 hour
# # of difference.
z = 0.25

def up_bound(x):
    return x + 0.25

def lw_bound(x):
    return x - 0.25

def generate_grid(ax, start=0, finish=1,
                  freqmajor = 1/2, freqminor=1/4,
                  colmajor: str='black', colminor: str='gray'):
    
    n_ticks = (finish-start) / freqminor

    ax.grid(which='major', color=colmajor, linewidth=1.2)
    ax.grid(which='minor', color=colminor, linewidth=0.6)
    ax.minorticks_on()
    ax.tick_params(which='minor', bottom=False, left=False)

    ax.xaxis.set_minor_locator(AutoMinorLocator(n_ticks))
    ax.yaxis.set_minor_locator(AutoMinorLocator(n_ticks)) 

    return ax



fig, ax = plt.subplots()
x = np.linspace(0, 1, num=100)
ax.plot(x, up_bound(x))
ax.plot(x, lw_bound(x))
ax = generate_grid(ax)
ax.set_xlim(min(x), max(x))
ax.set_ylim(min(x), max(x))

plt.savefig('mrs_x.png')