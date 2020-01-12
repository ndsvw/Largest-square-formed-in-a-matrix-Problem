# not a dynamic programming solution (it uses a bottom-up approach in calculate_longest_sequences, but is not actually dp)


def calculate_longest_sequences(matrix):
    """
    A method that calculates the largest square consisting of only 1's at the border of a given binary matrix
        time complexity: O(n*m*max(m,n))
        space complexity: O(m*n)

    Parameters
    ----------
    matrix : int[[]]
        a 2-dimensional list

    Returns
    -------
    (h, v)
        a tuple of two 2-dimensional lists:
        h: for every entry matrix[i][j] the longest hoirzontal sequence of '1's including matrix[i][j]
        v: for every entry matrix[i][j] the longest vertical sequence of '1's including matrix[i][j]
    """
    n = len(matrix)
    m = len(matrix[0])

    h = [[None for _ in range(m)] for _ in range(n)]
    v = [[None for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                h[i][j] = 0
                v[i][j] = 0
            else:
                h[i][j] = h[i][j-1] + 1 if j > 0 else 1
                v[i][j] = v[i-1][j] + 1 if i > 0 else 1
    return h, v


def calculate_largest_square_border(matrix):
    """
    A method that calculates the largest square consisting of only 1's at the border of a given binary matrix
        time complexity: O(n*m*max(m,n))
        space complexity: O(min(n,m))

    Parameters
    ----------
    matrix : int[[]]
        a 2-dimensional list

    Returns
    -------
    int
        size of the largest square with a border consisting of only 1's at the border
    """

    n = len(matrix)
    assert n >= 1
    m = len(matrix[0])
    assert m >= 1

    h_longest_seq, v_longest_seq = calculate_longest_sequences(matrix)

    max_square_length = 0
    for i in range(n):
        for j in range(m):
            h_seq = h_longest_seq[i][j]
            v_seq = v_longest_seq[i][j]
            longest_seq = min(h_seq, v_seq)
            if longest_seq >= 1:
                for k in range(longest_seq, 0, -1):
                    if h_longest_seq[i-(k-1)][j] >= k and v_longest_seq[i][j-(k-1)] >= k:
                        max_square_length = max(max_square_length, k)
                        break
    return max_square_length
