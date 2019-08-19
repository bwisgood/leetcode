class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        d = {}
        for i in range(len(nums)):
            c = target - nums[i]
            if d.get(c) is not None:
                return [d.get(c), i]
            d[nums[i]] = i


if __name__ == '__main__':
    s = Solution()
    r = s.twoSum([2, 7, 11, 15], 9)
    print(r)
