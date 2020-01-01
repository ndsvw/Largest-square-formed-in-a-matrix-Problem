import unittest
from largest_square_filled import calculate_largest_square_filled_first_approach, calculate_largest_square_filled_space_optimized1, calculate_largest_square_filled_space_optimized2


class Test(unittest.TestCase):

    def assert_filled_square_size_equals(self, matrix, size):
        sol1 = calculate_largest_square_filled_first_approach(matrix)
        sol2 = calculate_largest_square_filled_space_optimized1(matrix)
        sol3 = calculate_largest_square_filled_space_optimized2(matrix)
        self.assertEqual(sol1, size)
        self.assertEqual(sol2, size)
        self.assertEqual(sol3, size)

    def testAssertionError1(self):
        a = []
        self.assertRaises(
            AssertionError, calculate_largest_square_filled_first_approach, a)
        self.assertRaises(
            AssertionError, calculate_largest_square_filled_space_optimized1, a)
        self.assertRaises(
            AssertionError, calculate_largest_square_filled_space_optimized2, a)

    def testAssertionError2(self):
        a = [[]]
        self.assertRaises(
            AssertionError, calculate_largest_square_filled_first_approach, a)
        self.assertRaises(
            AssertionError, calculate_largest_square_filled_space_optimized1, a)
        self.assertRaises(
            AssertionError, calculate_largest_square_filled_space_optimized2, a)

if __name__ == "__main__":
    unittest.main()
