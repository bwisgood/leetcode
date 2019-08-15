class Solution:
    def removeDuplicates(self, nums: list) -> int:
        """
        nums = [1,2,2,3,4]
        :param nums:
        :return:
        """
        if not nums:
            return 0
        k = 1
        temp = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != temp:
                temp = nums[i]
                nums[k] = nums[i]
                k += 1
            if nums[i] == temp:
                continue
        return k


if __name__ == '__main__':
    s = Solution()
    r = s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
    print(r)
