from logging import config
import logging
from math import sqrt
from functools import reduce

config.fileConfig("src/config/logger.ini")


class Math:
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)

    def fibonacci_generator(self, ceil: int):
        fibonacci_seq = [1, 2]
        fib_values = [1, 2]
        fib_sum = 0
        while fib_sum < ceil:
            fib_sum = sum(fib_values)
            fib_values = [fib_values[1], fib_sum]
            if fib_sum < ceil:
                fibonacci_seq.append(fib_sum)
            else:
                break

        return fibonacci_seq

    def is_prime(self, num: int):
        result = True
        if num == 1:
            result = False
        else:
            for x in range (2, num):
                if num % x == 0:
                    result = False

        return result

    def get_prime_factors(self, num: int):
        # Code from StackOverflow (https://stackoverflow.com/questions/16007204/factorizing-a-number-in-python)
        # @ User: Will Ness
        # Notes: This performs significantly faster using yields and modifying the range on the fly.
        j = 2
        while num > 1:
            for i in range(j, int(sqrt(num))+1):
                if not num % i:
                    num //= i ; j = i
                    yield i
                    break
            else:
                if num > 1:
                    yield num; break

    def get_factors(self, num: int):
        factors =[1, num]
        j = 2
        while num > 1:
            for i in range (j, int(sqrt(num))+1):
                num //= i; j = i
                factors.append(i)
                factors.append(int(num/i))
                break
            else:
                if num > 1:
                    break
        return factors

    def square(self, num: int):
        return num*num

    def is_pythagorean(self, a: int, b: int, c: int):
        if self.square(a) + self.square(b) == self.square(c):
            return True
        else:
            return False

    def check_divisors(self, lower: int, upper: int, num: int):
        # Checks if all numbers in a range are divisors of a given number, num.
        for x in range(lower, upper):
            if not num % x:
                divisible = True
            else:
                return False
        if divisible == True:
            return divisible

    def check_palindrome(self, num: int):
        list_num = list(str(num))
        if not len(list_num) % 2:
            list_num_a = list_num[:len(list_num)//2]
            list_num_b = list(reversed(list_num[-len(list_num)//2:]))
        else:
            list_num_a = list_num[:len(list_num)//2+1]
            list_num_b = list(reversed(list_num[-len(list_num)//2:]))
        if list_num_a != list_num_b:
            return False
        return True

    def least_common_divisor(self, min: int, max: int):
        # AKA Least Common Multiple (LCM)
        prime_factors_dict = {}
        for x in range(min, max+1):
            if x != 1:
                prime_factors_dict[x] = list(self.get_prime_factors(x))

        prime_set = []
        for k, pfs in prime_factors_dict.items():
            prime_set += pfs
        prime_set = (set(prime_set))

        # For each prime less than range(max): check pf_dict for entry with the most times occurring in the list. Save prime to exponent.
        results = {}
        for prime in prime_set:
            count = 0
            for k, v in prime_factors_dict.items():
                if prime in v:
                    if v.count(prime) > count:
                        count = v.count(prime)
                    else:
                        pass
                results[prime] = count

        # Multiply all values together.
        result = 1
        for prime, power in results.items():
            result *= prime**power

        return result
