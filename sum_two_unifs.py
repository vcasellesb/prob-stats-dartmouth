import random
import matplotlib.pyplot as plt
import numpy as np

def get_one() -> float:
    return random.uniform(0, 1)

def simulate_one() -> float:
    x = get_one()
    y = get_one()
    return x+y

def main(niters: int) -> np.ndarray:
    res = np.zeros((niters))
    for _ in range(niters):
        z = simulate_one()
        res[_] = z
    return res

def plot_res(niters):
    res = main(niters)
    plt.hist(res, bins=11, density=True)
    plt.savefig('res2.png')

if __name__ == "__main__":
    plot_res(1000)