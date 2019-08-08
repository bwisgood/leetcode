class Solution:
    def findDiagonalOrder(self, matrix: list):
        M = len(matrix)
        if not M or not len(matrix[0]): return []
        N = len(matrix[0])
        row = col = 0
        result = []
        is_up = True
        while True:
            result.append(matrix[row][col])
            if row == M - 1 and col == N - 1:
                return result

            if is_up:
                if row == 0 and col < N - 1:
                    col += 1
                    is_up = False
                elif col == N - 1:
                    row += 1
                    is_up = False
                else:
                    row -= 1
                    col += 1
            else:
                if col == 0 and row < M - 1:
                    row += 1
                    is_up = True
                elif row == M - 1:
                    col += 1
                    is_up = True
                else:
                    row += 1
                    col -= 1
        return result


if __name__ == '__main__':
    s = Solution()
    r = s.findDiagonalOrder([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    print(r)
    """
    1  2  3  4
    5  6  7  8
    9  1  2  3
    4  5  6  7
    """
