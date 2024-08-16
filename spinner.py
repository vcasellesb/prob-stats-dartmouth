from typing import Dict
import numpy as np
import matplotlib.pyplot as plt

# example 2.1 https://math.dartmouth.edu/~prob/prob/prob.pdf and exercise 1 (page 52)
NITERATIONS = 1000000
r = 1
CIRCUMFERENCE = 2 * np.pi * r

lwr_bounds_1_2 = 0 * 1/2 * CIRCUMFERENCE
upr_bounds_1_2 = lwr_bounds_1_2 + 1/2 * CIRCUMFERENCE
lwr_bounds_1_3 = upr_bounds_1_2
upr_bounds_1_3 = lwr_bounds_1_3 + 1/3 * CIRCUMFERENCE
lwr_bounds_1_6 = upr_bounds_1_3
upr_bounds_1_6 = lwr_bounds_1_6 + 1/6 * CIRCUMFERENCE

assert np.round(upr_bounds_1_6, 7) == np.round(CIRCUMFERENCE, 7), f'{upr_bounds_1_6 = } \n {CIRCUMFERENCE = }'

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


def simulate(NITERATIONS: int) -> Dict[str, int]: 
    
    results = {
        '1/2': 0,
        '1/3': 0,
        '1/6': 0
    }

    for _ in range(NITERATIONS):
        x = np.random.uniform(0, 1) * CIRCUMFERENCE

        results['1/2'] += between(x, lwr_bound=lwr_bounds_1_2, upr_bound=upr_bounds_1_2)
        results['1/3'] += between(x, lwr_bound=lwr_bounds_1_3, upr_bound=upr_bounds_1_3)
        results['1/6'] += between(x, lwr_bound=lwr_bounds_1_6, upr_bound=upr_bounds_1_6)

    results = {k: v/NITERATIONS for k,v in results.items()}

    return results

def plot(results: Dict[str, int], fig_path: str):
    # generate plot as asked
    # from: https://stackoverflow.com/questions/70477458/how-can-i-plot-bar-plots-with-variable-widths-but-without-gaps-in-python-and-ad
    x = list(results.keys())
    cols = ['blue', 'red', 'grey']
    y_w_area = [get_height(convert_to_float(k), v) for k, v in results.items()]
    w = [convert_to_float(k) for k in results.keys()]
    xticks=[]
    for n, c in enumerate(w):
        xticks.append(sum(w[:n]) + w[n]/2)

    a = plt.bar(xticks, height = y_w_area, width = w, alpha = 0.8, color=cols)
    _ = plt.xticks(xticks, x)

    plt.legend(a.patches, x)
    plt.savefig(fig_path)

def main(NITERATIONS: int, fig_path: str):
    res = simulate(NITERATIONS)
    plot(res, fig_path)

if __name__ == "__main__":
    main(NITERATIONS, 'res_spinner.png')