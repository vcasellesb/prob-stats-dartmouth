import numpy as np
from typing import Dict
from utils import convert_to_float
import matplotlib.pyplot as plt

# example 2.9 https://math.dartmouth.edu/~prob/prob/prob.pdf

def throw_dart(r: float=1.0):
    
    x = np.random.uniform(0, r)
    y = np.random.uniform(0, r)

    pseudo_radius = np.sqrt((x**2) + (y**2))
    if pseudo_radius > r:
        return throw_dart(r)
    
    return x, y, pseudo_radius

def divide_circle(n: int=10, r: float=1):
    keys = list(range(1, n+1))
    keys = list(map(str, keys))

    f = np.cumsum([1/n * r for _ in range(n)])
    divided = {k: (v-(1/n * r), v) for k, v in zip(keys, f)}
    return divided

def main(n_splits: int, 
         r: float=1, 
         n_iterations: int=10000) -> Dict[str, int]:
    
    division = divide_circle(n_splits, r)
    lwr_bounds = sorted([b[0] for b in division.values()], reverse=True)

    results = {k: 0 for k in division.keys()}

    for i in range(n_iterations):
        x, y, d = throw_dart(r=r)
        res = [d > b for b in lwr_bounds]
        which = np.where(res)[0][0]
        
        results[str(n_splits - which)] += 1

    return {k: v/n_iterations for k, v in results.items()}, division

def plot(results: Dict[str, int], 
         width: float,
         fig_path: str='res_darts.png'):
    # generate plot as asked
    # from: https://stackoverflow.com/questions/70477458/how-can-i-plot-bar-plots-with-variable-widths-but-without-gaps-in-python-and-ad
    x = list(results.keys())
    bounds = ([1] + [convert_to_float(x_) for x_ in x])[::-1]
    y = [convert_to_float(v)/width for v in results.values()] 

    a = plt.bar(x, height = y, alpha = 0.8)
    _ = plt.xticks(x, [x_[:6] for x_ in x])

    plt.savefig(fig_path)

if __name__ == "__main__":

    results, division = main(n_splits=10)
    print(results)

    plot(results, width=1/10)