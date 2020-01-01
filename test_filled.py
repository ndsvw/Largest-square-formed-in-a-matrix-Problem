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

if __name__ == "__main__":
    unittest.main()
