import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from typing import Union

# Example 2.16
# let's say mr x arrives at time x, and mr y arrives at time y. We want to know the probability of
# x and y arriving at a z distance in time. If z==0, x and y arrive at the same time. If z==1 (z is
# upper bounded at 1, since they can only arrive with one hour of difference), they arrive with 1 hour
# # of difference.

def up_bound(x, z):
    return x + z

def lw_bound(x, z):
    return x - z

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


def main(z: Union[int, float],
         start: Union[int, float]=0,
         finish: Union[int, float]=1):
    fig, ax = plt.subplots()
    x = np.linspace(start, finish, num=100)
    ax.plot(x, up_bound(x, z))
    ax.plot(x, lw_bound(x, z))
    ax.plot(x, x*1, color='black')
    ax = generate_grid(ax, start, finish)
    ax.fill_between(x, x - z, x + z, facecolor='C0', alpha=0.4)
    ax.set_xlim(min(x), max(x))
    ax.set_ylim(min(x), max(x))
    probability_cdf = 1 - (1-z)**2
    bbox = dict(boxstyle='round', fc='blanchedalmond', ec='orange', alpha=1)
    rang = (finish - start)
    plt.text(x = rang / 2 - rang * 1/20, y = (finish - start)/2, fontsize=10, s=f'P = {probability_cdf}', bbox=bbox)
    plt.savefig(f'mrs_xy_z_{str(z).replace(".", "_")}.png')

if __name__ == "__main__":
    main(z=0.5, start=0, finish=1)