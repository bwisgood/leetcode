class Solution:
    def intersection(self, nums1: list, nums2: list) -> list:
        return list(set(nums1) & set(nums2))


if __name__ == '__main__':
    s = Solution()
    r = s.intersection([4, 9, 5], [9, 4, 9, 8, 4])
    print(r)
