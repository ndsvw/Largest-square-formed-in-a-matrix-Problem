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


def calculate_largest_square_filled_space_optimized1(matrix):
    """
    A method that calculates the largest square filled with only 1's of a given binary matrix (space-optimized 1/2).
    Problem description: https://practice.geeksforgeeks.org/problems/largest-square-formed-in-a-matrix/0
        time complexity: O(n*m)
        space complexity: O(m)

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

    arr = [
        [0 for _ in range(m)],
        [0 for _ in range(m)]
    ]

    max_square_size = 0

    for i in range(n):
        arr[0] = [e for e in arr[1]]
        for j in range(m):
            if matrix[i][j] == 0:
                arr[1][j] = 0
            else:
                if i == 0 or j == 0:
                    arr[1][j] = 1
                else:
                    arr[1][j] = min([
                        arr[0][j],
                        arr[1][j-1],
                        arr[0][j-1]
                    ]) + 1
                max_square_size = max(arr[1][j], max_square_size)
    return max_square_size

