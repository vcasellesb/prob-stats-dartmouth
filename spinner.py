from typing import Dict
import numpy as np
import matplotlib.pyplot as plt
from utils import convert_to_float, area_bar_graph

# example 2.1 https://math.dartmouth.edu/~prob/prob/prob.pdf and exercise 1 (page 52)

def between(x: float, lwr_bound: float, upr_bound: float) -> bool:
    return lwr_bound <= x < upr_bound
    
def get_height(width: float, p: float):
    # area = a*b
    # we have area, which is p, and width
    return p / width

def simulate(*bounds, circumference: float, niterations: int) -> Dict[str, int]:
    bounds = [convert_to_float(b) for b in bounds]
    
    assert np.round(sum(bounds), 10) == 1, sum(bounds)
    if bounds[0] != 0:
        bounds = [0] + bounds
    ps = list(np.array(bounds[1:]))
    bounds = sorted(list(np.cumsum(np.array(bounds) * circumference)), reverse=True)
    
    # initialize results
    results = {str(p): 0 for p in ps}
    
    for _ in range(niterations):
        x = np.random.uniform(0, 1) * circumference
        for i, b in enumerate(bounds[1:]):
            this_p = str(ps[::-1][i])            
            if x > b:
                results[this_p] += 1
                break       

    results = {k: v/niterations for k,v in results.items()}
    return results

def plot(results: Dict[str, int], fig_path: str):
    # generate plot as asked
    # from: https://stackoverflow.com/questions/70477458/how-can-i-plot-bar-plots-with-variable-widths-but-without-gaps-in-python-and-ad
    x = list(results.keys())
    y_w_area = [get_height(convert_to_float(k), v) for k, v in results.items()]
    widths = [convert_to_float(k) for k in results.keys()]
    xticks = [sum(widths[:(n+1)]) for n in range(len(widths)-1)]
    
    xticks = [0] + xticks
    print(xticks)

    area_bar_graph(ticks=xticks, areas = list(results.values()), 
                   heights=y_w_area, widths=widths, alpha=0.8, color=list(results.keys()), save_path=fig_path)

def main(*bounds, niterations: int, fig_path: str, circumference: float) -> None:
    res = simulate(*bounds, circumference=circumference, niterations=niterations)
    plot(res, fig_path)

if __name__ == "__main__":
    NITERATIONS = 1000000
    r = 1
    CIRCUMFERENCE = 2 * np.pi * r
    main(1/3, 1/4, 1/5, 1/6, 1/20, niterations=NITERATIONS, fig_path='res_spinner.png', circumference=CIRCUMFERENCE)