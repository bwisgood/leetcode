class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1]) if s else ""


if __name__ == '__main__':
    s = Solution()
    r = s.reverseWords("")
    print(":%s:" % r)
