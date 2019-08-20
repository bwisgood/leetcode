class Solution:
    def intersect(self, nums1: list, nums2: list) -> list:
        # return list(set(nums1) & set(nums2))
        # 遍历nums1 和 nums2
        common = []
        for i in nums1:
            if i in nums2:
                common.append(i)
                nums2.remove(i)
        return common


if __name__ == '__main__':
    s = Solution()
    r = s.intersect([1, 2, 2, 3], [2, 2])
    print(r)
