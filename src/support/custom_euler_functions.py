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

    def get_largest_palindromic_number_as_product(self, lower: int, upper: int):
        # Function for Euler Problem 4
        set_a = list(range(lower, upper+1))
        set_b = list(range(lower, upper+1))
        cross_prod = [i*j for i in set_a for j in set_b]
        palindromes = filter(lambda i: Math().check_palindrome(i), cross_prod)
        return max(palindromes)

    def get_smallest_multiple_of_range(self, lower: int, upper: int):
        multi_range = list(range(lower, upper+1))
        range_factor_dict = {}
        # Get the prime factorization of all numbers in range
        for x in multi_range:
            if x != 1:
                range_factor_dict[x] = list(Math().get_prime_factors(x))
        self.logger.info(range_factor_dict)

    def get_sum_square_difference(self, lower: int, upper:int):
        # Function for Euler Problem 6
        sum_of_squares = 0
        for x in range (lower, upper+1):
            sum_of_squares+=Math().square(x)

        square_of_sums = 0
        for x in range(lower, upper+1):
            square_of_sums += x
        square_of_sums = Math().square(square_of_sums)

        self.logger.info(sum_of_squares)
        self.logger.info(square_of_sums)
        return square_of_sums - sum_of_squares

    def get_nth_prime(self, n: int):
        val = 1
        ctr = 0
        while ctr < n+1:
            if Math().is_prime(val):
                ctr+=1
            if ctr == n:
                return val
            val+=1

    def get_largest_prod_in_series(self, num_adjacent_digits: int):
        big_number = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
        list_big_number = list(str(big_number))
        list_products = []
        for x in range(0, len(list_big_number)-num_adjacent_digits):
            tmp_prod = 1
            for y in range(1, num_adjacent_digits+1):
                tmp_prod *= int(list_big_number[int(x)+int(y)])
            list_products.append(tmp_prod)
        return max(list_products)
