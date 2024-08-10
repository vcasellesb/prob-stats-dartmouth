import random
from typing import Tuple, Union
import numpy as np

# Example 2.6 https://math.dartmouth.edu/~prob/prob/prob.pdf
# Note: the length of a chord is given by 2 * √(r^2 - d^2) where d is the line that
# bisects the chord

def rectangular_coord() -> Tuple[float, float]:
    x = random.uniform(-1, 1) # actually, it doesn't matter if its [0, 1] or [-1, 1]
    y = random.uniform(-1, 1)
    return x, y

def polar_coord_midpoint() -> float:
    r = random.uniform(0, 1)
    return r

def polar_coord_endpoints() -> float:
    alpha = random.uniform(0, 2*np.pi)
    return alpha

def main(niters: int, 
         mode: int,
         enforce_niters: bool=True) -> Union[float, Tuple[float, int]]:
    res = 0
    true_iters = 0

    # in case we choose mode of random chord drawing 1, some iterations will not produce a valid midpoint
    # this line enforces that niters iterations are actually run
    if mode == 1 and enforce_niters:
        niters_true = niters
        niters *= 99999999999999999 # basically infinite loop
    
    # the why behind the differences between methods are beautifully explained here
    # https://www.uio.no/studier/emner/matnat/math/MAT4010/data/forelesningsnotater/w-bertrand-paradox-(probability).pdf
    for i in range(niters):
        match mode:
            case 1:
                x, y = rectangular_coord()
                if (x**2) + (y**2) > 1:
                    # we are outside circle, so next iter
                    continue
                decision = (2 * np.sqrt((1 - ((x**2) + (y**2))))) > np.sqrt(3)
                res += decision
                true_iters += 1  
                if enforce_niters and true_iters == niters_true:
                    # we have reached the desired niters, so breaking out
                    break
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
    
    return (res/true_iters, true_iters) if mode == 1 else res/niters


if __name__ == "__main__":

    results = main(10000, mode=1, enforce_niters=False)
    print(results)