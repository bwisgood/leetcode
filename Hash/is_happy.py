class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        def _next(number):
            base = 0
            while number:
                number, i = divmod(number, 10)
                base += i ** 2
            return base

        def dfs(c, visited):
            if c == 1:
                return True
            next_ = _next(c)
            if next_ in visited:
                return False
            else:
                visited.add(next_)
            return dfs(next_, visited)

        return dfs(n, visited)


if __name__ == '__main__':
    s = Solution()
    r = s.isHappy(19)
    print(r)
