class Solution:
    def arrayPairSum(self, nums: list) -> int:
        nums.sort()
        base = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                base += nums[i]
        return base


if __name__ == '__main__':
    s = Solution()
    r = s.arrayPairSum([1, 2, 3, 4])
    print(r)
