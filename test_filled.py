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

    def testSimpleCase1(self):
        a = [
            [0]
        ]
        self.assert_filled_square_size_equals(a, 0)

    def testSimpleCase2(self):
        a = [
            [1]
        ]
        self.assert_filled_square_size_equals(a, 1)

    def testSimpleCase3(self):
        a = [
            [1, 1],
            [1, 1]
        ]
        self.assert_filled_square_size_equals(a, 2)

    def testSimpleCase4(self):
        a = [
            [0, 0],
            [0, 0]
        ]
        self.assert_filled_square_size_equals(a, 0)

    def testSimpleCase5(self):
        a = [
            [1, 0],
            [0, 0]
        ]
        self.assert_filled_square_size_equals(a, 1)

    def testSimpleCase6(self):
        a = [
            [0, 1],
            [0, 0]
        ]
        self.assert_filled_square_size_equals(a, 1)

    def testSimpleCase7(self):
        a = [
            [0, 0],
            [1, 0]
        ]
        self.assert_filled_square_size_equals(a, 1)

    def testSimpleCase8(self):
        a = [
            [0, 0],
            [0, 1]
        ]
        self.assert_filled_square_size_equals(a, 1)

    def testSimpleCase9(self):
        a = [
            [1, 1]
        ]
        self.assert_filled_square_size_equals(a, 1)

    def test3x3Nr1(self):
        a = [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]
        self.assert_filled_square_size_equals(a, 1)

    def test3x3Nr2(self):
        a = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        self.assert_filled_square_size_equals(a, 3)

    def test3x3Nr3(self):
        a = [
            [1, 0, 1],
            [0, 1, 1],
            [1, 1, 1]
        ]
        self.assert_filled_square_size_equals(a, 2)

    def test5x6(self):
        a = [
            [0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1]
        ]
        self.assert_filled_square_size_equals(a, 3)

    def test6x5(self):
        a = [
            [1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1]
        ]
        self.assert_filled_square_size_equals(a, 3)

    def test_large1(self):
        a = [
            [0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
        ]
        self.assert_filled_square_size_equals(a, 6)

    def test_large2(self):
        a = [
            [0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
            [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
            [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1],
            [1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
            [0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0],
            [1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0],
            [1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1],
            [0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0],
            [1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0],
            [1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1],
            [1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1],
            [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1],
            [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0],
            [0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
            [0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1],
            [1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
            [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1],
            [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0],
            [1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
            [1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1],
            [0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0],
            [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1],
            [0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0],
            [0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1]
        ]
        self.assert_filled_square_size_equals(a, 2)

    def test_large3_horizontal(self):
        a = [
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.assert_filled_square_size_equals(a, 6)

    def test_large3_vertical(self):
        a = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.assert_filled_square_size_equals(a, 6)


if __name__ == "__main__":
    unittest.main()
