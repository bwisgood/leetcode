class Solution:
    def findMaxConsecutiveOnes(self, nums: list) -> int:
        max_ = 0
        k = 0
        l = len(nums)
        for i, e in enumerate(nums):
            if e == 1:
                k += 1
                if i == l - 1:
                    max_ = max(k, max_)

            elif e == 0:
                max_ = max(k, max_)
                k = 0
        return max_


if __name__ == '__main__':
    s = Solution()
    r = s.findMaxConsecutiveOnes([0])
    print(r)
