import unittest
from euler.euler_problems import Euler
from robber import expect


class EulerTestCases(unittest.TestCase):
    def test_euler_problem_1_soln(self):
        output = Euler().problem_1()
        expect(output).to.eq(233168)

    def test_euler_problem_2_soln(self):
        # Unverified
        output = Euler().problem_2()
        expect(output).to.eq(4613732)

    def test_euler_problem_3_soln_example(self):
        output = Euler().problem_3(
            num=13195
        )
        expect(output).to.eq(29)

    def test_euler_problem_3_soln(self):
        # Not Tested, long runtime
        output = Euler().problem_3(
            num=600851475143
        )
        expect(output).to.eq(6857)

    def test_euler_problem_4_soln(self):
        output = Euler().problem_4()
        expect(output).to.eq(906609)

    def test_euler_problem_5(self):
        output = Euler().problem_5(
            lower=1,
            upper=20
        )
        expect(output).to.eq(232792560)

    def test_euler_problem_5_soln_example(self):
        output = Euler().problem_5(
            lower=1,
            upper=10
        )
        expect(output).to.eq(2520)

    def test_euler_problem_6_soln_example(self):
        output = Euler().problem_6(
            lower=1,
            upper=10
        )
        expect(output).to.eq(2640)

    def test_euler_problem_6_soln(self):
        # Unverified
        output = Euler().problem_6(
            lower=1,
            upper=100
        )
        expect(output).to.eq(25164150)

    def test_euler_problem_7_soln_example(self):
        output = Euler().problem_7(
            n=6
        )
        expect(output).to.eq(13)

    """def test_euler_problem_7_soln(self):
        # Not tested, long runtime
        output = Euler().problem_7(
            pos=10001
        )
        expect(output).to.eq(0)"""

    def test_euler_problem_8_soln_example(self):
        output = Euler().problem_8(
            num_adjacent_digits=4
        )
        expect(output).to.eq(5832)

    """def test_euler_problem_8_soln(self):
        # Untested
        output = Euler().problem_8(
            adj_digits=13
        )
        expect(output).to.eq(0)"""

    def test_euler_problem_9_soln_example(self):
        output = Euler().problem_9(
            triplet_sum=12
        )
        expect(output).to.eq(60)

    """def test_euler_problem_9_soln(self):
        output = Euler().problem_9(
            triplet_sum=1000
        )
        expect(output).to.eq([0,0,0])"""
    pass
