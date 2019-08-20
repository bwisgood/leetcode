class Solution:
    def firstUniqChar(self, s: str) -> int:
        # d = {e: 0 for i, e in enumerate(s)}
        # print(d)
        d = {}
        for i, e in enumerate(s):
            if e in d:
                d[e] += 1
            else:
                d[e] = 0

        for i in filter(lambda x: x[1] == 0, d.items()):
            return s.find(i[0])
        return -1


if __name__ == '__main__':
    s = Solution()
    r = s.firstUniqChar("")
    print(r)
