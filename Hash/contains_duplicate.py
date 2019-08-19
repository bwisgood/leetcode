class Solution:
    def containsDuplicate(self, nums: list) -> bool:
        s = set()
        for i in nums:
            if i not in s:
                s.add(i)
            else:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    r = s.containsDuplicate([1, 2, 3, 4, 5, 5])
    print(r)
