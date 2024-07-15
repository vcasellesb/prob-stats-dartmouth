import numpy as np

def sample_d() -> float:
    """
    Sample distance of center of needle to one of the lines
    """
    return np.random.uniform(low=0.0, high=1/2)

def sample_theta() -> float:
    """
    Sample orientation of needle. theta is the acute angle of the needle wrt the set of parallel lines
    It is higher bounded at pi/2 (90º), lower bounded at 0.
    """
    return np.random.uniform(low=0.0, high=np.pi/2)

def sim_1needle() -> bool:

    left = sample_d() / np.sin(sample_theta())
    right = 1/2

    return left < right

def buffons_needle(n_iters: int):
    res = 0
    for _ in range(n_iters):
        res += sim_1needle()
    
    P = res/n_iters
    print(f'Needle crossed parallel lines {res}/{n_iters} times, yielding a probability of {P}')
    expected = f'{2/np.pi}'
    print(f'We would have expected:', expected)


buffons_needle(n_iters=100000)