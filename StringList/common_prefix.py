class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        if not strs:
            return ""

        # if len(strs) == 1:
        #     return strs[0]

        def find(c, x, l):
            if x > len(c):
                return strs[0]
            print(c[:x])
            l = list(filter(lambda y: y.startswith(c[:x]), l))
            print(l)
            if len(l) != len(strs):
                return c[:x - 1]
            else:
                return find(c, x + 1, l)

        # z = strs.pop(0)
        return find(strs[0], 0, strs)


if __name__ == '__main__':
    s = Solution()
    r = s.longestCommonPrefix(["f"])
    print(":", r)
