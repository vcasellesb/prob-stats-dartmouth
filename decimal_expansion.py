from collections.abc import Callable
# Geometric series
n = 1000
num = 0
for i in range(0, n):
    num += 1 * 2 ** -i
    
# print(num)

f = lambda x: (x**2) - 12*x + 35

assert f(2) > 0
assert f(3) > 0
assert f(4) > 0 
assert f(4.9) > 0
assert f(5) == 0
assert f(6) < 0
assert f(7) == 0
assert f(7.2) > 0

# fancy way of doing these
def assert_multiple_conditions(f: Callable, 
                               lower_lim, 
                               upper_lim,
                               interval_: float = 0.1,
                               rounding_error = 2):
    
    x = lower_lim
    while x < upper_lim:
        x = round(x, rounding_error)
        z = f(x)
        condition_to_assert = z > 0 if (x < 5 or x > 7) else z <= 0
        assert condition_to_assert, f'\n{x = }\n{z = }'
        x += interval_

if __name__ == "__main__":
    assert_multiple_conditions(
        f = f,
        lower_lim=2,
        upper_lim=10
    )