import numpy as np
from utils.utils import Number


def sample_exponential_density(lambda_: Number, size: int=None) -> float:
    
    if not size:
        size = 1
    
    return (-1/lambda_) * np.log(np.random.uniform(size=size))