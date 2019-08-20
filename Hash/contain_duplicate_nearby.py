class Solution:
    def containsNearbyDuplicate(self, nums: list, k: int) -> bool:
        d = {}

        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = i
            else:
                x = i - d[nums[i]]
                if x <= k:
                    return True
                else:
                    d[nums[i]] = i
        return False


if __name__ == '__main__':
    s = Solution()
    # r = s.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], k=2)
    # r = s.containsNearbyDuplicate(nums=[1, 0, 1, 1], k=1)
    r = s.containsNearbyDuplicate(nums=[1, 2, 3, 1], k=3)
    print(r)
