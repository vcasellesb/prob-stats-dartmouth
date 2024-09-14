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
        

def exercise_8(section: str, niters: int=10_000) -> None:
    bs = np.random.uniform(size=niters)
    cs = np.random.uniform(size=niters)

    match section.lower():
        case 'a':
            # triangle with 1/2 sides
            condition_array = (bs + cs) < 1/2
        case 'b':
            condition_array = (bs * cs) < 1/2
        case 'c':
            condition_array = np.abs(bs - cs) < 1/2
        case 'd':
            condition_array = np.maximum(bs, cs) < 1/2
        case 'e':
            condition_array = np.minimum(bs, cs) < 1/2
        case 'f':
            c1 = bs < 1/2
            c2 = (1 - cs) < 1/2 # essentially boils down ot cs > 1/2
            c2_test = cs > 1/2
            assert (c2 == c2_test).all()
            condition_array = np.logical_and(c1, c2)
        case 'g':
            c1 = np.abs(bs - cs) < 1/2
            c2_1 = bs < 1/2 
            c2_2 = (1 - cs) < 1/2
            condition_array = np.logical_and.reduce((c1, c2_1, c2_2))
        case 'h':
            condition_array = (bs ** 2) + (cs ** 2) < 1/2
        case 'i':
            condition_array = ((bs - 1/2)**2) + ((cs - 1/2)**2) < 1/4
        case _:
            raise NotImplementedError
        
    return np.sum(condition_array) / niters

if __name__ == "__main__":
    tol_ = 0.05
    
    ex_a = exercise_7('a')
    assert np.abs(ex_a - 1/3) < tol_, f'{ex_a = }'

    ex_b = exercise_7('b')
    assert np.abs(ex_b - 1/2) < tol_, f'{ex_b = }'

    ex_c = exercise_7('c')
    # clearly this should be 1/2
    assert np.abs(ex_c - 1/2) < tol_, f'{ex_c = }'

    ex_d = exercise_7('d')
    assert np.abs(ex_d - 1/3) < tol_, f'{ex_d = }'

    ex_8_a = exercise_8('a')
    should_be_ex_8_a = ((1/2) ** 2) / 2 # triangle with 1/2 sides
    assert np.abs(ex_8_a - should_be_ex_8_a) < tol_, f'{ex_8_a = }'

    ex_8_b = exercise_8('b')
    should_be_ex_8_b = 1/2 + (-np.log(1/2))/2 # jesus fucking christ I had to plot this one
    assert np.abs(ex_8_b - should_be_ex_8_b) < tol_, f'{ex_8_b = }'

    ex_8_c = exercise_8('c')
    should_be_ex_8_c = 1 - ((1/2)**2) # 3/4 essentially
    assert np.abs(ex_8_c - should_be_ex_8_c) < tol_, f'{ex_8_c = }'

    ex_8_d = exercise_8('d')
    should_be_ex_8_d = 1/4 # logic, both are independent events with P = 1/2
    assert np.abs(ex_8_d - should_be_ex_8_d) < tol_, f'{ex_8_d}'
    
    ex_8_e = exercise_8('e')
    should_be_ex_8_e = 3/4
    assert np.abs(ex_8_e - should_be_ex_8_e) < tol_, f'{ex_8_e = }'

    ex_8_f = exercise_8('f')
    should_be_ex_8_f = 1/4 # equivalent to d
    assert np.abs(ex_8_f - should_be_ex_8_f) < tol_, f'{ex_8_f = }'

    ex_8_g = exercise_8('g')
    should_be_ex_8_g = 1/8
    assert np.abs(ex_8_g - should_be_ex_8_g) < tol_, f'{ex_8_g = }'

    ex_8_h = exercise_8('h')
    should_be_ex_8_h = np.pi / 8
    assert np.abs(ex_8_h - should_be_ex_8_h) < tol_, f'{ex_8_h = }'

    ex_8_i = exercise_8('i')
    should_be_ex_8_i = np.pi / 4
    assert np.abs(ex_8_i - should_be_ex_8_i) < tol_, f'{ex_8_i = }'