from sieve import sieve_prime_generator


def test_calculation():
    assert list(sieve_prime_generator(100)) == [
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
        73,
        79,
        83,
        89,
        97,
    ]


def test_last_number_in_range():
    assert list(sieve_prime_generator(11)) == [2, 3, 5, 7, 11]
