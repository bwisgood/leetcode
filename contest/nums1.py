class Solution:
    def isMajorityElement(self, nums: list, target: int) -> bool:
        l = len(nums)
        times = 0

        for e in nums:
            if e == target:
                times += 1

            if times > l / 2:
                break

        return times > l / 2


if __name__ == '__main__':
    s = Solution()
    r = s.isMajorityElement([2, 4, 5, 5, 5, 5, 5, 6, 6], 5)
    print(r)
