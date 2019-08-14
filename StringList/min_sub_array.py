class Solution:
    def minSubArrayLen(self, s: int, nums: list) -> int:
        # 超时
        l = len(nums)

        if not nums:
            return 0

        min_ = 0
        for i in range(l):
            k = 0
            sum_ = 0
            for j in range(i, l):
                sum_ += nums[j]
                k += 1
                if sum_ >= s:
                    if min_ == 0:
                        min_ = k
                    else:
                        min_ = min(k, min_)
        return min_


if __name__ == '__main__':
    s = Solution()
    r = s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
    print(r)
