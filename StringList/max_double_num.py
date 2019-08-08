class Solution:
    def dominantIndex(self, nums: list) -> int:
        if len(nums) == 1:
            return 0
        c_max = 0
        c_double_max = True
        for i in range(1, len(nums)):
            if nums[i] == 0:
                continue
            if nums[i] >= nums[c_max]:
                if not nums[c_max] or nums[i] // nums[c_max] >= 2:
                    c_double_max = True
                else:
                    c_double_max = False
                c_max = i

            else:
                if nums[c_max] // nums[i] < 2:
                    c_double_max = False
        return c_max if c_double_max else -1


if __name__ == '__main__':
    s = Solution()
    r = s.dominantIndex([0, 0, 0, 1])
    print(r)
    r = s.dominantIndex([3, 6, 1, 0])
    print(r)
    r = s.dominantIndex([1, 2, 3, 4])
    print(r)
    r = s.dominantIndex([1])
    print(r)
    r = s.dominantIndex([1, 0])
    print(r)
