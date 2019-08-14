class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k


if __name__ == '__main__':
    s = Solution()
    n = [1, 2, 3, 32, 32, 13, 12, 3, 3, 3, 3]
    r = s.removeElement(n, 3)
    for i in range(r):
        print(n[i])
