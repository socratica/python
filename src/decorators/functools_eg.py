import time
from functools import wraps


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Δt = {end_time - start_time:.4f}")
        return result
    return wrapper


############################################################
##### Test the wraps decorator in the functools module #####
def do_nothing(f):
    # @wraps(f)
    def inner(*args, **kwargs):
        return f(*args, **kwargs)
    return inner


# @do_nothing
def alpha(*args, **kwargs):
    """A function for viewing the arguments."""
    print(f'args = {args}')
    print(f'kwargs = {kwargs}')


alpha('a', 2, None, x=7, y=11, z=26)
print(alpha.__name__)
print(alpha.__doc__)
############################################################


###################################################################
##### Demonstrate the cache decorator in the functools module #####
from functools import cache

# @cache
def fibonacci(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError(f"{n} not a positive integer")

    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# for i in range(1, 10):
#     print(fibonacci(i))


@timer
def global_fibonacci(n):
    return fibonacci(n)

# for n in range(1, 34):
#     nth_term = global_fibonacci(n)
#     print(f"Fibonacci({n}) = {nth_term}")
###################################################################