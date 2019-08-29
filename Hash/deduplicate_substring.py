class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        ans, i, j = 0, 0, 0
        hash_ = set()

        while i < l and j < l:
            # 延伸窗口
            if not s[j] in hash_:
                hash_.add(s[j])
                j += 1
                ans = max(ans, j - i)
            else:
                hash_.remove(s[i])
                i += 1

        return ans


if __name__ == '__main__':
    s = Solution()
    r = s.lengthOfLongestSubstring("")
    print(r)
