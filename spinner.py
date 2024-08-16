from typing import Dict
import numpy as np
import matplotlib.pyplot as plt

# example 2.1 https://math.dartmouth.edu/~prob/prob/prob.pdf and exercise 1 (page 52)

def between(x: float, lwr_bound: float, upr_bound: float) -> bool:
    return lwr_bound <= x < upr_bound

def convert_to_float(frac_str: str):
    try:
        return float(frac_str)
    except ValueError:
        try:
            num, denom = frac_str.split('/')
        except ValueError:
            return None
        try:
            leading, num = num.split(' ')
        except ValueError:
            return float(num) / float(denom)        
        if float(leading) < 0:
            sign_mult = -1
        else:
            sign_mult = 1
        return float(leading) + sign_mult * (float(num) / float(denom))
    
def get_height(width: float, p: float):
    # area = a*b
    # we have area, which is p, and width
    return p / width


def simulate(*bounds, CIRCUMFERENCE: float, NITERATIONS: int) -> Dict[str, int]:
    bounds = [convert_to_float(b) for b in bounds]
    
    assert np.round(sum(bounds), 10) == 1, sum(bounds)
    if bounds[0] != 0:
        bounds = [0] + bounds
    ps = list(np.array(bounds[1:]))
    bounds = sorted(list(np.cumsum(np.array(bounds) * CIRCUMFERENCE)), reverse=True)
    
    # initialize results
    results = {str(p): 0 for p in ps}
    
    for _ in range(NITERATIONS):
        x = np.random.uniform(0, 1) * CIRCUMFERENCE
        for i, b in enumerate(bounds[1:]):
            this_p = str(ps[::-1][i])            
            if x > b:
                results[this_p] += 1
                break       

    results = {k: v/NITERATIONS for k,v in results.items()}
    return results

def plot(results: Dict[str, int], fig_path: str):
    # generate plot as asked
    # from: https://stackoverflow.com/questions/70477458/how-can-i-plot-bar-plots-with-variable-widths-but-without-gaps-in-python-and-ad
    x = list(results.keys())
    y_w_area = [get_height(convert_to_float(k), v) for k, v in results.items()]
    w = [convert_to_float(k) for k in results.keys()]
    xticks=[]
    for n, c in enumerate(w):
        xticks.append(sum(w[:n]) + w[n]/2)

    a = plt.bar(xticks, height = y_w_area, width = w, alpha = 0.8, color=list(results.keys()))
    _ = plt.xticks(xticks, x)

    plt.legend(a.patches, x)
    plt.savefig(fig_path)

def main(*bounds, NITERATIONS: int, fig_path: str, CIRCUMFERENCE: float) -> None:
    res = simulate(*bounds, CIRCUMFERENCE=CIRCUMFERENCE, NITERATIONS=NITERATIONS)
    plot(res, fig_path)

if __name__ == "__main__":
    NITERATIONS = 1000000
    r = 1
    CIRCUMFERENCE = 2 * np.pi * r
    main('1/3', '1/4', '1/5', '1/6', '1/20', NITERATIONS=NITERATIONS, fig_path='res_spinner.png', CIRCUMFERENCE=CIRCUMFERENCE)