import numpy as np

# https://math.dartmouth.edu/~prob/prob/prob.pdf
# chapter 2

def l2_norm(point1: np.ndarray, point2: np.ndarray):

    return np.sqrt(np.sum((point1 - point2) ** 2))

def simulate_circle_one(r: float = 1/2):
    """
    Circle of r = 1/2, with center in (1/2, 1/2) (in two dimensions)
    check if a random point in a square with area 1 falls within circle
    """

    # draw random point within a area 1 square, start at (0, 0), "end" at (1, 1)
    x_and_y = np.random.uniform(size=2)

    return l2_norm(x_and_y, np.array([1/2, 1/2])) <= r

def simulate_circle(N_SIM = 10_000):
    accuracy = 1/np.sqrt(N_SIM) # 1/100
    
    res = 0
    for i in range(N_SIM):
        res += simulate_circle_one(r = 1/2)
    
    # we would expect that pi/4 of times the point would fall within circle
    expected_P = np.pi / 4
    actual_P = np.sum(res) / N_SIM

    print(f'{expected_P = }')
    print(f'{actual_P = }')

    assert abs(expected_P - actual_P) < accuracy, f'{abs(expected_P - actual_P)=}, {accuracy=}'

    return actual_P


def estimate_pi(n_times: int=10_000):

    P_E = simulate_circle(N_SIM=n_times)

    print(f'Estimated pi is:')
    print(f'{4 * P_E}')


def test_l2norm():
    point1 = np.array([1, 1])
    point2 = np.array([2, 2])
    assert l2_norm(point1, point2) == np.sqrt(2), f'{l2_norm(point1, point2) = }'
    assert l2_norm(point1, point1) == 0.0


if __name__ == "__main__":
    estimate_pi(n_times=10_000)
