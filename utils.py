import numpy as np
import numpy.typing as npt
from typing import Union
import matplotlib.pyplot as plt

Number = Union[int, float]

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
    
def convert_to_fraction(float_: float, m: int) -> str:
    """
    m: number of decimal digits to consider

    See:
        https://github.com/python/cpython/blob/main/Lib/fractions.py

    """
    n = 0
    p = float_

    while p - np.floor(p) > 0 and n <= m:
        p *= 10
        n += 1

    r = gcd(p, 10**n)
    p = p/r
    q = 10**n / r

    return f'{p}/{q}'
    
def gcd(a: int, b: int) -> int:

    "Returns greatest common denominator between a and b"

    while b != 0:
        r = a % b
        a = b
        b = r
    
    return a

def area_bar_graph(areas: npt.ArrayLike,
                   ticks: npt.ArrayLike,
                   save_path: str,
                   widths: npt.ArrayLike = None,
                   heights: npt.ArrayLike = None,
                   **kwargs_bar):
    
    assert len(areas) == len(ticks)

    if widths is None:
        width = ticks[1] - ticks[0]
        assert all([ticks[i+1] - ticks[i] == width for i in range(1, len(ticks)-1)]), 'Widths are expected to be all of the same length'
        widths = [width] * len(areas)
    if heights is None:
        heights = [a/width for a in areas]
    
    plt.bar(ticks, height=heights, width=widths, **kwargs_bar)
    plt.savefig(save_path)
    

if __name__ == "__main__":
    assert gcd(25, 10) == 5
    assert gcd(96, 72) == 24
    assert gcd(4, 2) == 2


    float1 = 0.333000000001
    assert convert_to_fraction(float1, m=1) == "1/5", convert_to_fraction(float1, 1)