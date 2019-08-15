class Solution:
    def generate(self, numRows: int) -> list:
        base = [[1], [1, 1]]
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return base

        for i in range(2, numRows):
            temp = [1 for _ in range(i + 1)]
            for j in range(i + 1):
                try:
                    if j - 1 < 0:
                        continue
                    temp[j] = base[i - 1][j - 1] + base[i - 1][j]
                except IndexError:
                    pass
            print(temp)
            base.append(temp)
        return base


if __name__ == '__main__':
    s = Solution()
    r = s.generate(5)
    print(r)
