from logging import config
import logging
from support.custom_euler_functions import CustomEulerFunction
from support.math import Math

config.fileConfig("src/config/logger.ini")


class Euler:
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)

    def problem_1(self, lower=1, upper=1000, multiple_a=3, multiple_b=5):
        # Instruction: Find the sum of all multiples of 3 or 5 below 1000
        problem_1_soln = CustomEulerFunction().sum_of_multiples(
            lower=int(lower),
            upper=int(upper),
            multiple_a=int(multiple_a),
            multiple_b=int(multiple_b)
        )
        return problem_1_soln

    def problem_2(self, fibonacci_lim=4000000):
        # Instruction: Find sum of even valued terms in Fibonacci sequence.
        problem_2_soln = CustomEulerFunction().get_sum_evens_fibonacci_seq(
            fibonacci_lim=int(fibonacci_lim)
        )
        return problem_2_soln

    def problem_3(self, num=600851475143):
        # Instruction: Largest Prime Factor of 600851475143
        problem_3_soln = CustomEulerFunction().get_largest_prime_factor(
            num=int(num)
        )
        return problem_3_soln

    def problem_4(self, lower=100, upper=999):
        # Instrution: Largest Palindromic Number as product of two 3-digit numbers
        problem_4_soln = CustomEulerFunction().get_largest_palindromic_number_as_product(
            lower=int(lower),
            upper=int(upper)
        )
        return problem_4_soln

    def problem_5(self, lower=1, upper=20):
        # Instruction: Smallest Multiple: smallest positive number that is evenly divisble by all numbers in range (1,20)
        problem_5_soln = Math().least_common_divisor(
            min=int(lower),
            max=int(upper)
        )
        return problem_5_soln

    def problem_6(self, lower: int, upper: int):
        # Instruction: Sum Square Difference: Find the difference between the sum of the squares of the first 100 natural numbers and the square of that sum.
        problem_6_soln = CustomEulerFunction().get_sum_square_difference(
            lower=int(lower),
            upper=int(upper)
        )
        return problem_6_soln

    def problem_7(self, n=1001):
        # Instruction: 10001st Prime
        problem_7_soln = CustomEulerFunction().get_nth_prime(
            n = int(n)
        )
        return problem_7_soln

    def problem_8(self, num_adjacent_digits=4):
        problem_8_soln = CustomEulerFunction().get_largest_prod_in_series(
            num_adjacent_digits=int(num_adjacent_digits)
        )
        return problem_8_soln

    def problem_9(self, triplet_sum: int):
        for x in range(1, triplet_sum-3):
            a = x
            b = x + 1
            c = x + 2
            if Math().is_pythagorean(a=a, b=b, c=c) and a+b+c==triplet_sum:
                return a*b*c
        return []
