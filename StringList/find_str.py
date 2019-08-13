class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0
        if not haystack:
            return -1
        if not needle:
            return 0

        l = len(needle)
        lh = len(haystack)
        for i in range(lh):
            if i + l == lh:
                if haystack[i:i + l] != needle:
                    return -1
            if i + l > lh:
                return -1
            # print(haystack[i:i + l])
            if haystack[i:i + l] == needle:
                return i


if __name__ == '__main__':
    s = Solution()
    r = s.strStr("mississippi", "pi")
    "mississippi"
    "pi"
    print(r)
