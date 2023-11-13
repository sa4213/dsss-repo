import unittest
import random
from math_quiz import get_integer, get_sign, calculation


class TestMathGame(unittest.TestCase):

    def test_function_get_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = get_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_get_sign(self):
        random.seed(42) # everytime the same sign gets selected if the methodes works correctly
        sign = get_sign()
        self.assertTrue(sign == '*')

    def test_function_calculation(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (7, 8, '*', '7 * 8', 56),
                (3, 1, '-', '3 - 1', 2),
            ]
            # Test if each case gets calculated correctly
            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = calculation(num1, num2, operator)
                self.assertTrue(problem == expected_problem and answer == expected_answer)
                

if __name__ == "__main__":
    unittest.main()
