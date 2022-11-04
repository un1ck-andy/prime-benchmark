def sieve_prime_generator(max_value: int):
    """Generate primes up to N using Sieve of Eratosthenes"""
    multiples: set = set()
    for number in range(2, max_value + 1):
        if number not in multiples:
            yield number
            multiples.update(range(number * number, max_value + 1, number))
