from logging import config
import logging
from support.custom_euler_functions import CustomEulerFunction
from support.math import Math

config.fileConfig("src/config/logger.ini")


class Euler:
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)

    def problem_1(self):
        # Instruction: Find the sum of all multiples of 3 or 5 below 1000
        problem_1_soln = CustomEulerFunction().sum_of_multiples(
            lower=1,
            upper=1000,
            multiple_a=3,
            multiple_b=5
        )
        return problem_1_soln

    def problem_2(self):
        # Instruction: Find sum of even valued terms in Fibonacci sequence.
        problem_2_soln = CustomEulerFunction().get_sum_evens_fibonacci_seq(
            fibonacci_lim=4000000
        )
        return problem_2_soln

    def problem_3(self):
        # Instruction: Largest Prime Factor of 600851475143
        problem_3_soln = CustomEulerFunction().get_largest_prime_factor(
            num=600851475143
        )
        return problem_3_soln

    def problem_4(self):
        # Instrution: Largest Palindromic Number as product of two 3-digit numbers
        problem_4_soln = CustomEulerFunction().get_largest_palindromic_number_as_product(
            lower=100,
            upper=999
        )
        return problem_4_soln

    def problem_5(self):
        # Instruction: Smallest Multiple: smallest positive number that is evenly divisble by all numbers in range (1,20)
        problem_5_soln = CustomEulerFunction().get_smallest_multiple_of_range(
            lower=1,
            upper=20
        )
        return problem_5_soln

    def problem_6(self, lower: int, upper: int):
        # Instruction: Sum Square Difference: Find the difference between the sum of the squares of the first 100 natural numbers and the square of that sum.
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

    def problem_7(self, pos: int):
        # Instruction: 10001st Prime
        val = 1
        ctr = 0
        while ctr < pos+1:
            if Math().is_prime(val):
                ctr+=1
            if ctr == pos:
                return val
            val+=1

    def problem_8(self, adj_digits: int):
        big_number = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
        list_big_number = list(str(big_number))
        list_products = []
        for x in range(0, len(list_big_number)-adj_digits):
            tmp_prod = 1
            for y in range(1, adj_digits+1):
                tmp_prod *= int(list_big_number[int(x)+int(y)])
            list_products.append(tmp_prod)
        return max(list_products)

    def problem_9(self, triplet_sum: int):
        for x in range(1, triplet_sum-3):
            a = x
            b = x + 1
            c = x + 2
            if Math().is_pythagorean(a=a, b=b, c=c) and a+b+c==triplet_sum:
                return a*b*c
        return []
