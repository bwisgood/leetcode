class Solution:
    def numSquares(self, n: int) -> int:
        from math import sqrt
        from queue import Queue
        seen = set()
        if sqrt(n).is_integer():
            return 1
        step = -1
        q = Queue()
        max_ = int(sqrt(n))
        q.put(0)
        while not q.empty():
            step += 1
            for size in range(q.qsize()):
                cur = q.get()
                if cur == n:
                    return step

                for i in range(max_, -1, -1):
                    temp = cur + (i + 1) * (i + 1)
                    if temp <= n and temp not in seen:
                        seen.add(temp)
                        q.put(temp)


if __name__ == '__main__':
    solution = Solution()
    print(solution.numSquares(318))
