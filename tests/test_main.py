import pytest

import main


def test_output():
    assert main.benchmark_sieve_prime_generator(100) == [
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
    assert main.benchmark_brute_prime_generator(100) == [
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


def test_input_int(capsys):
    main.main(["-n 10"])
    out, err = capsys.readouterr()
    assert out == ""
    assert err == ""


def test_input_string(capsys):
    with pytest.raises(SystemExit) as excinfo:
        main.main(["asd"])
    (retv,) = excinfo.value.args
    assert retv == 2
    out, err = capsys.readouterr()
    assert (
        err
        == "usage: pytest [-h] [-n NUMBER]\npytest: error: unrecognized arguments: asd\n"
    )


def test_empty_input_int():
    with pytest.raises(SystemExit) as excinfo:
        main.main()
    (retv,) = excinfo.value.args
    assert retv == "Missing command-line argument, use -h for help"
