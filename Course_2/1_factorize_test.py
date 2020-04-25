import unittest


def factorize(x):
    """
    Factorize positive integer and return its factors.
    :type x: int,>=0
    :rtype: tuple[N],N>0
    """
    pass


class TestFactorize:

    def test_wrong_types_raise_exception(self):
        'string',  1.5
        pass

    def test_negative(self):
        -1, -10, -100
        pass

    def test_zero_and_one_cases(self):
        0 ? (0,), 1 ? (1,)
        pass

    def test_simple_numbers(self):
        3 ? (3,), 13 ? (13,), 29 ? (29,)
        pass

    def test_two_simple_multipliers(self):
        6 ? (2, 3),   26 ? (2, 13),   121 --> (11, 11)
        pass

    def test_many_multipliers(self):
        1001 ? (7, 11, 13), 9699690 ? (2, 3, 5, 7, 11, 13, 17, 19)
        pass

