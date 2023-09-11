import unittest
from support.custom_euler_functions import CustomEulerFunction
from robber import expect


class CustomEulerFunctionTestCases(unittest.TestCase):
    def test_sum_of_multiples(self):
        output = CustomEulerFunction().sum_of_multiples(
            lower=1,
            upper=10,
            multiple_a=3,
            multiple_b=5
        )
        expect(output).to.eq(23)

    def test_get_largest_prime_factor(self):
        output = CustomEulerFunction().get_largest_prime_factor(
            num=13195
        )
        expect(output).to.eq(29)

    def test_get_largest_palindromic_number_as_product(self):
        output = CustomEulerFunction().get_largest_palindromic_number_as_product(
            lower=10,
            upper=100
        )
        expect(output).to.eq(9009)

