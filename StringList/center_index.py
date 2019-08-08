class Solution:
    def pivotIndex(self, nums) -> int:
        # 直接计算会超时，需要保存当前的before和end
        nums_len = len(nums)

        if nums_len < 3:
            return -1
        before = 0
        end = sum(nums)
        for i in range(nums_len):
            if i == 0:
                before = nums[0]
                # continue
            else:
                before += nums[i - 1]
                end -= nums[i]
            if before == end:
                return i
        return -1


if __name__ == '__main__':
    s = Solution()
    r = s.pivotIndex([-1,-1,-1,0,1,1])
    print(r)
