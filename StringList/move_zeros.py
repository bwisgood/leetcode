class Solution:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        for i in range(l):
            if nums[i] == 0:
                j = i + 1
                while j < l:
                    if nums[j] != 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
                    j += 1
        for i in nums:
            print(i)

    def moveZeroes1(self, nums: list) -> None:
        k = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1
        for j in range(k, len(nums)):
            nums[j] = 0
        for i in nums:
            print(i)


if __name__ == '__main__':
    s = Solution()
    s.moveZeroes([0, 1, 0, 3, 12])
    s.moveZeroes1([0, 1, 0, 3, 12])
