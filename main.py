import argparse
import concurrent.futures
import sys
import time
from typing import Optional
from typing import Sequence

from brute import brute_prime_generator
from sieve import sieve_prime_generator


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Run parallel benchmark which algorithm is faster"""

    # arguments usage implementation
    parser = argparse.ArgumentParser(    )
    parser.add_argument(
        "-n",
        "--number",
        help="the maximum value to which the calculation will be carried out",
    )
    args = parser.parse_args(argv)

    # A command-line argument the max value (N)
    if args == None:
        sys.exit("Missing command-line argument, use -h for help")
    # If that argument cannot be converted to an int, the program should exit with an error message.
    try:
        max_value: int = int(args.number)
    except ValueError:
        sys.exit("Command-line argument is not a number, use -h for help")
    # Making a list of our algorithms
    funcs: list = [benchmark_brute_prime_generator, benchmark_sieve_prime_generator]
    # start the parallel run
    with concurrent.futures.ProcessPoolExecutor() as pool:
        for func in funcs:
            pool.submit(func, max_value)
    return 1



def benchmark_sieve_prime_generator(max_value: int) -> int:
    # just to kickstart generator and count time
    start_time: float = time.perf_counter()
    result: list = list(sieve_prime_generator(max_value))
    end_time: float = time.perf_counter()
    run_time: float = end_time - start_time
    print(
        f"{run_time:.10f} seconds to generate primes up to {max_value} with Sieve"
    )


def benchmark_brute_prime_generator(max_value: int) -> int:
    # just to kickstart generator and count time
    start_time: float = time.perf_counter()
    result: list = list(brute_prime_generator(max_value))
    end_time: float = time.perf_counter()
    run_time: float = end_time - start_time
    print(
        f"{run_time:.10f} seconds to generate primes up to {max_value} with Bruteforce"
    )


if __name__ == "__main__":
    sys.exit(main())
