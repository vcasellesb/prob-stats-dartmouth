import random
from typing import Tuple
import numpy as np

# Example 2.6 https://math.dartmouth.edu/~prob/prob/prob.pdf
# Note: the length of a chord is given by 2 * √(r^2 - d^2) where d is the line that
# bisects the chord

def rectangular_coord() -> Tuple[float, float]:
    x = random.uniform(-1, 1) # actually, it doesn't matter if its [0, 1] or [-1, 1]
    y = random.uniform(-1, 1)
    return x, y

def polar_coord_midpoint():
    r = random.uniform(0, 1)
    return r

def polar_coord_endpoints():
    alpha = random.uniform(0, 2*np.pi)
    return alpha

def main(niters: int, mode: int) -> None:
    res = 0
    true_iters = 0
    # the why behind the differences between methods are beautifully explained here
    # https://www.uio.no/studier/emner/matnat/math/MAT4010/data/forelesningsnotater/w-bertrand-paradox-(probability).pdf
    for i in range(niters):
        match mode:
            case 1:
                x, y = rectangular_coord()
                if (x**2) + (y**2) > 1:
                    # we are outside circle
                    continue
                decision = (2 * np.sqrt((1 - ((x**2) + (y**2))))) > np.sqrt(3)
                res += decision
                true_iters += 1  
            case 2:
                r = polar_coord_midpoint()
                decision = (2 * np.sqrt(1 - (r**2))) > np.sqrt(3)
                res += decision
            case 3:
                alpha = polar_coord_endpoints()
                decision = (np.sqrt(2 - 2 * np.cos(alpha))) > np.sqrt(3)
                res += decision

            case _:
                raise ValueError
    
    return res/true_iters if mode == 1 else res/niters


if __name__ == "__main__":

    results = main(10000, mode=1)
    print(results)