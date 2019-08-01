class Solution:
    def numSquares(self, n: int) -> int:
        from math import sqrt
        step = 1
        max_ = int(sqrt(n))
        cur = n - max_ ** 2
        print(max_, "+")
        while cur != 0:
            max_ = int(sqrt(max_))
            print(max_, "+")
            cur = cur - max_ ** 2
            step += 1
        return step


if __name__ == '__main__':
    solution = Solution()
    print(solution.numSquares(12))
