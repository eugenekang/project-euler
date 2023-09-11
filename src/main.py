import logging
import sys
from logging import config

sys.path.append('src')

from euler.euler_problems import Euler

config.fileConfig("src/config/logger.ini")


def main():
    logger = logging.getLogger(__name__)
    logger.info("Beginning Euler Problem Solving...")
    euler = Euler()
    logger.info(f"Euler Problem 1 Solution: {euler.problem_1()}")
    logger.info(f"Euler Problem 2 Solution: {euler.problem_2()}")
    logger.info(f"Euler Problem 3 Solution: {euler.problem_3()}")
    logger.info(f"Euler Problem 4 Solution: {euler.problem_4()}")
    logger.info(f"Euler Problem 5 Solution: {euler.problem_5()}")


if __name__ == "__main__":
    main()
