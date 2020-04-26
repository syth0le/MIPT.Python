import unittest


def factorize(x):
    """
    Factorize positive integer and return its factors.
    :type x: int,>=0
    :rtype: tuple[N],N>0
    """
    pass


class TestFactorize(unittest.TestCase):

    def test_wrong_types_raise_exception(self):
        tests = ('string', 1.5)
        for test in tests:
            with self.subTest(x=test):
                self.assertRaises(TypeError, factorize, test)

    def test_negative(self):
        tests = (-1, -10, -100)
        for test in tests:
            with self.subTest(x=test):
                self.assertRaises(ValueError, factorize, test)

    def test_zero_and_one_cases(self):
        tests = (0, 1)
        for test in tests:
            with self.subTest(x=test):
                self.assertEqual(factorize(test), (test,))

    def test_simple_numbers(self):
        tests = (3, 13, 29)
        for test in tests:
            with self.subTest(x=test):
                self.assertEqual(factorize(test), (test,))

    def test_two_simple_multipliers(self):
        test_cases = (
            (6, (2, 3)),
            (26, (2, 13)),
            (121, (11, 11)),
        )
        for x, expected in test_cases:
            with self.subTest(x=x):
                self.assertEqual(factorize(x), expected)

    def test_many_multipliers(self):
        test_cases = (
            (1001, (7, 11, 13)),
            (9699690, (2, 3, 5, 7, 11, 13, 17, 19)),
        )
        for x, expected in test_cases:
            with self.subTest(x=x):
                self.assertEqual(factorize(x), expected)
