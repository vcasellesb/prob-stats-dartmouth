import numpy as np

def exercise_7(section: str, niters:int=10_000):
    bs = np.random.uniform(size=niters)

    match section:
        case 'a':
            return np.sum(np.logical_and(bs > 1/3, bs < 2/3)) / niters
        case 'b':
            return np.sum(np.abs(bs - 1/2) <= 1/4) / niters
        case 'c':
            return np.sum(np.logical_or(bs < 1/4, 1-bs<1/4)) / niters
        case 'd':
            return np.sum(3 * (bs**2) < bs) / niters
        case _:
            raise NotImplementedError


if __name__ == "__main__":
    ex_a = exercise_7('a')
    assert np.abs(ex_a - 1/3) < 0.05, f'{ex_a = }'

    ex_b = exercise_7('b')
    assert np.abs(ex_b - 1/2) < 0.05, f'{ex_b = }'

    ex_c = exercise_7('c')
    # clearly this should be 1/2
    assert np.abs(ex_c - 1/2) < 0.05, f'{ex_c = }'

    ex_d = exercise_7('d')
    assert np.abs(ex_d - 1/3) < 0.05, f'{ex_d = }'