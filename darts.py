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

def main(n_splits: int, 
         r: float=1, 
         n_iterations: int=10000) -> Dict[str, int]:
    
    factor_list = ([0] + list(np.cumsum([1/n_splits * 1] * (n_splits - 1))))[::-1]
    bounds = np.cumsum([1/n_splits * r] * (n_splits - 1))
    bounds_list = ([0] + list(bounds))[::-1]

    results = {str(round(f, 2)):0 for f in factor_list}

    for i in range(n_iterations):
        x, y, d = throw_dart(r=r)
        res = [d > b for b in bounds_list]
        which = np.where(res)[0][0]
        
        results[str(round(factor_list[which], 2))] += 1

    return {k: v/n_iterations for k, v in results.items()}

def plot(results: Dict[str, int], fig_path: str='res_darts.png'):
    # generate plot as asked
    # from: https://stackoverflow.com/questions/70477458/how-can-i-plot-bar-plots-with-variable-widths-but-without-gaps-in-python-and-ad
    x = list(results.keys())[::-1]
    bounds = ([1] + [convert_to_float(x_) for x_ in x])[::-1]
    y = [convert_to_float(v) for v in results.values()][::-1]

    a = plt.bar(x, height = y, alpha = 0.8, color=list(results.keys()))
    _ = plt.xticks(x, [x_[:6] for x_ in x])

    plt.savefig(fig_path)
 



if __name__ == "__main__":
    results = main(n_splits=10)

    plot(results)
