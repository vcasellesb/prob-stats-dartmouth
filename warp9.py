from typing import List
import numpy as np
from utils.utils import Number, area_bar_graph


def divide_sample_space(values: np.ndarray, 
                        nsplits: Number = 10,
                        max_ = None, 
                        min_ = None):
    
    if max_ is None:
        max_ = max(values)
    if min_ is None:
        min_ = min(values)

    width = (max_ - min_) / nsplits
    tmp_ticks = [0 + width * i for i in range(nsplits + 1)][::-1]

    f = lambda x: np.where(x > tmp_ticks)[0][0]
    which_bins = np.array(list(map(f, values)))
    which_bins = [nsplits - i for i in which_bins if i != 0] # we remove any value over 100
    ticks = tmp_ticks[1:][::-1]
    return which_bins, ticks

def area_bar_graph_helper(bins: List, ticks: List, 
                   niters: int, save_path: str):
    
    assert save_path.endswith('.png') # should we even check this?
    
    res = dict((x, bins.count(x) / niters) for x in set(bins))
    areas = list(res.values())

    area_bar_graph(areas=areas, ticks=ticks, save_path=save_path)

def simulate_xs_ys(lambd: Number, niters: int):
    rands = np.random.rand(niters)
    xs = - (1/lambd) * np.log(rands)
    repeats = np.sum((xs <= 15))

    while repeats > 0:
        tmp = - (1/lambd) * np.log(np.random.rand(repeats))
        xs[xs<=15] = tmp
        repeats = np.sum((xs<=15))
    
    return xs, xs - 15

if __name__ == "__main__":

    xs, ys = simulate_xs_ys(lambd=1/30, niters=10_000)

    bins_y, ticks = divide_sample_space(ys, nsplits=10, max_=100, min_=0)

    area_bar_graph_helper(bins=bins_y, ticks=ticks, niters=10_000, save_path='res_warp9.png')