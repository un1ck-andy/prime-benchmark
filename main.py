import argparse
import concurrent.futures
import os
import sys
from typing import Optional
from typing import Sequence

from algorithms.brute import brute_prime_generator
from algorithms.sieve import sieve_prime_generator
from time_wrapper import time_it


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Run parallel benchmark which algorithm is faster"""

    # arguments usage implementation
    parser = argparse.ArgumentParser(
        description="""
        Benchmark tests for prime numbers calculation algorithms in parallel
        """,
        epilog="""
                                         Usage example:
                                         python {} -n 100
                                         """.format(
            os.path.basename(__file__)
        ),
    )
    parser.add_argument(
        "-n",
        "--number",
        help="the maximum value to which the calculation will be carried out",
    )
    args = parser.parse_args(argv)

    # A command-line argument the max value (N)
    if args.number is None:
        sys.exit("Missing command-line argument, use -h for help")
    # If argument is not int, the program should exit with an error message.
    try:
        max_value: int = int(args.number)
    except ValueError:
        sys.exit("Command-line argument is not a number, use -h for help")

    # Making a list of our algorithms
    funcs: list = [
        benchmark_brute_prime_generator,
        benchmark_sieve_prime_generator,
    ]
    # start the parallel run
    with concurrent.futures.ProcessPoolExecutor() as pool:
        for func in funcs:
            pool.submit(func, max_value)
    return 1


@time_it
def benchmark_sieve_prime_generator(max_value: int) -> int:
    # just to kickstart generator
    result: list = list(sieve_prime_generator(max_value))
    return result


@time_it
def benchmark_brute_prime_generator(max_value: int) -> int:
    # just to kickstart generator
    result: list = list(brute_prime_generator(max_value))
    return result


if __name__ == "__main__":
    sys.exit(main())
