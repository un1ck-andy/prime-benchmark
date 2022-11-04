from functools import wraps
import time


def time_it(func):
    @wraps(func)
    def time_it_wrapper(*args):
        start_time: float = time.perf_counter()
        result = func(*args)
        end_time: float = time.perf_counter()
        run_time: float = end_time - start_time
        print(
            f"{run_time:.10f} seconds to generate primes up to {args[0]} with {func.__name__}"
        )
        return result

    return time_it_wrapper
