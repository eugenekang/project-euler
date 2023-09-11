from logging import config
import logging
from support.math import Math
import math

config.fileConfig("src/config/logger.ini")


class CustomEulerFunction:
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)

    def sum_of_multiples(self, lower: int, upper: int, multiple_a: int, multiple_b: int):
        # Function for Euler Problem 1
        sum = 0
        for i in range(lower, upper):
            if i % multiple_a == 0 or i % multiple_b == 0:
                sum += i
        return sum

    def get_sum_evens_fibonacci_seq(self, fibonacci_lim: int):
        # Function for Euler Problem 2
        fib_seq = Math().fibonacci_generator(fibonacci_lim)
        sum_fib = sum(n for n in fib_seq if not n % 2)
        return sum_fib

    def get_largest_prime_factor(self, num: int):
        # Function for Euler Problem 3
        prime_factors = Math().get_prime_factors(num)
        return max(list(prime_factors))

    """def get_largest_palindromic_number_as_product(self, lower: int, upper: int):
        # Function for Euler Problem 4
        palindromic_prods = []
        for x in range(upper-1, lower, -1):
            for y in range(upper-1, lower, -1):
                product = x*y
                if Math().check_palindrome(product):
                    palindromic_prods.append(product)
        if palindromic_prods:
            return max(palindromic_prods)
        else:
            return None"""

    def get_largest_palindromic_number_as_product(self, lower: int, upper: int):
        # Function for Euler Problem 4
        set_a = list(range(lower, upper+1))
        set_b = list(range(lower, upper+1))
        cross_prod = [i*j for i in set_a for j in set_b]
        palindromes = filter(lambda i: Math().check_palindrome(i), cross_prod)
        return max(palindromes)


    """def get_smallest_multiple_of_range(self, lower: int, upper: int):
        # Function for Euler Problem 5
        max_value = 1
        for x in range(lower, upper+1):
            max_value *= x
        for x in range(lower, max_value):
            if Math().check_divisors(lower, upper, x):
                return x"""

    def get_smallest_multiple_of_range(self, lower: int, upper: int):
        multi_range = list(range(lower, upper+1))
        range_factor_dict = {}
        # Get the prime factorization of all numbers in range
        for x in multi_range:
            if x != 1:
                range_factor_dict[x] = list(Math().get_prime_factors(x))
        self.logger.info(range_factor_dict)


        """prime_multi_range = list(filter(lambda x: Math().is_prime(x), multi_range))
        self.logger.info(f"Primes: {prime_multi_range}")

        i = 1
        while i > 0:
            # Perform same mod operation to entire list of primes
            result = list(map(lambda x : i % x, mul_range))
            # Check if set is exactly 0
            list_result = list(set(result))
            if len(list_result) == 1 and list_result[0] == 0:
                return i
            i += 1"""





