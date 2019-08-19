class Solution:
    def singleNumber(self, nums: list) -> int:
        # 空间复杂度=n
        nums.sort()
        l = len(nums)
        if l < 2:
            return nums[0]

        for i in range(l):
            if i % 2 == 0:
                if i + 1 > l - 1 or nums[i] != nums[i + 1]:
                    return nums[i]

    def other1(self, nums: list) -> int:
        s1 = set()
        s2 = set()
        for i in nums:
            if i not in s1:
                s1.add(i)
            else:
                s2.add(i)
        c = s1.difference(s2)
        if not c:
            return nums[0]
        return c.pop()


if __name__ == '__main__':
    s = Solution()
    r = s.other1([2,2,1])
    print(r)
