import time
from functools import wraps


def time_it(func):
    @wraps(func)
    def time_it_wrapper(*args):
        start_time: float = time.perf_counter()
        result = func(*args)
        end_time: float = time.perf_counter()
        run_time: float = end_time - start_time
        print(
            f"{run_time:.10f}s to get primes <={args[0]} with {func.__name__}"
        )
        return result

    return time_it_wrapper
