class Solution:
    def rotate(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        [1, 2, 3, 4, 5, 6, 7], 3
        ||
        \/
        [5, 6, 7, 1, 2, 3, 4]
        l = len(nums)
        1. 遍历range(k)
        2  让temp = i
        3. 让第i个和第(i+k)/l数字交换
        4. 第(i+k)/l就等于previous
        5. 让temp+k/l
        """
        # temp = 0
        # for i in range(k):
        #     temp = i
        #     while temp %
        print(nums)
        l = len(nums)
        if l < 2 or k == 0 or k == l:
            return
        i = -1
        step = 0
        while step != l:
            i += 1
            temp = (i + k) % l
            pre = nums[i]
            while True:
                nums[temp], pre = pre, nums[temp]
                temp = (temp + k) % l
                step += 1
                if temp == i:
                    break
            nums[i] = pre
            step += 1
        print(nums)


if __name__ == '__main__':
    s = Solution()
    r = s.rotate([1, 2, 3, 4, 5, 6], 2)
    # print(r)
    # s.rotate([1, 2, 3], 3)
