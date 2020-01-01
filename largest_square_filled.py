from functools import reduce

# a dynamic programming solution


def calculate_largest_square_filled_first_approach(matrix):
    """
    A method that calculates the largest square filled with only 1's of a given binary matrix (not space-optimized).
    Problem description: https://practice.geeksforgeeks.org/problems/largest-square-formed-in-a-matrix/0
        time complexity: O(n*m)
        space complexity: O(n*m)

    Parameters
    ----------
    matrix : int[[]]
        a 2-dimensional list

    Returns
    -------
    int
        size of the largest square
    """

    n = len(matrix)
    assert n >= 1
    m = len(matrix[0])
    assert m >= 1

    arr = [[None for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                arr[i][j] = 0
            else:
                if i == 0 or j == 0:
                    arr[i][j] = 1
                else:
                    arr[i][j] = min([
                        arr[i-1][j],
                        arr[i][j-1],
                        arr[i-1][j-1]
                    ]) + 1
    return max(reduce(lambda e, f: e + f, arr, []))

