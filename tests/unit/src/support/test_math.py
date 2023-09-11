import unittest
from support.math import Math
from robber import expect


class MathTestCases(unittest.TestCase):
    def test_fibonacci_generator(self):
        output = Math().fibonacci_generator(100)
        expect(output).to.eq([1,2,3,5,8,13,21,34,55,89])

    def test_is_prime_true(self):
        output = Math().is_prime(13)
        expect(output).to.eq(True)

    def test_is_prime_false(self):
        output = Math().is_prime(800)
        expect(output).to.eq(False)

    """def test_get_factors(self):
        output = Math().get_factors(24)
        expect(list(output)).to.eq([1,2,3,4,6,8,12,24])"""

    def test_square(self):
        output = Math().square(4)
        expect(output).to.eq(16)

    def test_check_divisors_true(self):
        output = Math().check_divisors(
            lower=1,
            upper=10,
            num=2520
        )
        expect(output).to.eq(True)

    def test_check_divisors_false(self):
        output = Math().check_divisors(
            lower=1,
            upper=10,
            num=13
        )
        expect(output).to.eq(False)

    def test_check_palindrome_true(self):
        output = Math().check_palindrome(1234321)
        expect(output).to.eq(True)

    def test_check_palindrome_false(self):
        output = Math().check_palindrome(990009)
        expect(output).to.eq(False)

    def test_get_least_common_divisor(self):
        output = Math().least_common_divisor(
            min = 1,
            max = 10
        )
        expect(output).to.eq(2520)
