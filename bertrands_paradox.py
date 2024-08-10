import random
from typing import Tuple, Union
import numpy as np

# Example 2.6 https://math.dartmouth.edu/~prob/prob/prob.pdf
# Note: the length of a chord is given by 2 * √(r^2 - d^2) where d is the line that
# bisects the chord

def rectangular_coord(radius: Union[int, float]) -> Tuple[float, float]:
    x = random.uniform(-radius, radius) # actually, it doesn't matter if its [0, radius] or [-radius, radius]
    y = random.uniform(-radius, radius)
    return x, y

def polar_coord_midpoint(radius: Union[int, float]) -> float:
    r = random.uniform(-radius, radius) # it does not matter wether we choose between [0, radius] or [-radius, radius] either
    return r

# why does it not matter wether we choose x/y or r from [-radius,radius] or [0,radius] uniforms?
# well, it's actually because their value does not matter until they are plugged in the bisector
# length formula, which esentially squares them. Thus, the results you get from -0.5 are the same as from 0.5.

def polar_coord_endpoints(trick: bool=True) -> float:
    alpha = random.uniform(0, 2*np.pi)
    if not trick:
        beta = random.uniform(0, 2*np.pi)
        return alpha, beta
    return alpha

def main(niters: int, 
         mode: int,
         enforce_niters: bool=True,
         trick_mode_3: bool=True,
         radius: Union[float, int]=1) -> Union[float, Tuple[float, int]]:
    res = 0
    true_iters = 0

    # in case we choose mode of random chord drawing 1, some iterations will not produce a valid midpoint
    # this line enforces that niters iterations are actually run
    if mode == 1 and enforce_niters:
        niters_to_enforce = niters
        niters *= 99999999999999999 # basically infinite loop
    
    # the why behind the differences between methods are beautifully explained here
    # https://www.uio.no/studier/emner/matnat/math/MAT4010/data/forelesningsnotater/w-bertrand-paradox-(probability).pdf
    for i in range(niters):
        match mode:
            case 1:
                x, y = rectangular_coord(radius=radius)
                if np.sqrt((x**2) + (y**2)) > radius:
                    # we are outside circle, so next iter
                    continue
                decision = (2 * np.sqrt(((radius**2) - ((x**2) + (y**2))))) > np.sqrt(3) * radius
                res += decision
                true_iters += 1  
                if enforce_niters and true_iters == niters_to_enforce:
                    # we have reached the desired niters, so breaking out
                    break
            case 2:
                r = polar_coord_midpoint(radius)
                decision = (2 * np.sqrt((radius**2) - (r**2))) > np.sqrt(3) * radius
                res += decision
            case 3:
                # trick controls wether beta is fixed at 0 angles (endpoint at coordinates [0, 1])
                # or if it's randomly chosen same as alpha. To check whether it's the same
                alpha = polar_coord_endpoints(trick=trick_mode_3)
                if not trick_mode_3:
                    alpha, beta = alpha
                    angle = np.abs(alpha - beta)
                    # from: https://www.quora.com/How-do-we-find-the-length-of-an-arc-from-its-end-points-and-the-chord-that-contains-it
                    decision = (2 * radius * np.sin(angle/2)) > np.sqrt(3) * radius
                else:
                    # as established in the original document
                    decision = (np.sqrt((radius**2) + (radius**2) - (2 * radius * radius * np.cos(alpha)))) > np.sqrt(3) * radius
                res += decision

            case _:
                raise ValueError(f'Invalid method for randomly drawing a chord. Choose from 1, 2 or 3. Got \'{mode}\'.')
    
    return (res/true_iters, true_iters) if mode == 1 else res/niters


if __name__ == "__main__":

    results = main(1000000, 
                   mode=2, 
                   radius=1, 
                   trick_mode_3=False)
    print(results)