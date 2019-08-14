class Solution:
    def minSubArrayLen(self, s: int, nums: list) -> int:
        import sys
        MAX_INT = sys.maxsize
        k = 0
        sum_ = 0
        min_ = MAX_INT
        for i in range(len(nums)):
            sum_ += nums[i]
            while sum_ >= s:
                min_ = min(min_, i - k + 1)
                sum_ -= nums[k]
                k += 1
        return min_ if min_ != MAX_INT else 0


if __name__ == '__main__':
    s = Solution()
    r = s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
    print(r)
