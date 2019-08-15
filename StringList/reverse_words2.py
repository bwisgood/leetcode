class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(map(lambda x: x[::-1], s.split())) if str else ""


if __name__ == '__main__':
    s = Solution()
    r = s.reverseWords("ab")
    print(":%s:" % r)
