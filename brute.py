def brute_prime_generator(max_value: int):
    """Generate primes up to N using brute force"""
    for i in range(2, max_value + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            yield i
