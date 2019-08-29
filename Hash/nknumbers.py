class Solution:
    def topKFrequent(self, nums: list, k: int) -> list:

        if len(nums) == 1:
            return nums

        i = 0
        j = len(nums) - 1

        # 一个用来存每个元素以及对应出现的次数{element: times}
        d1 = {}
        # 另一个用来存次数对应的值{times: [element1, element2]}
        d2 = {}

        while i <= j:
            # 先看i
            if nums[i] in d1:
                d1[nums[i]] += 1
            else:
                d1[nums[i]] = 1
            # 加入d2
            if d1[nums[i]] in d2:
                d2[d1[nums[i]]].append(nums[i])
            else:
                d2[d1[nums[i]]] = [nums[i]]
            # 移除之前添加的
            if d1[nums[i]] != 1:
                d2[d1[nums[i]] - 1].remove(nums[i])

            i += 1
            # 再看j
            if nums[j] in d1:
                d1[nums[j]] += 1
            else:
                d1[nums[j]] = 1
            # 加入d2
            if d1[nums[j]] in d2:
                d2[d1[nums[j]]].append(nums[j])
            else:
                d2[d1[nums[j]]] = [nums[j]]
            # 移除之前添加的
            if d1[nums[j]] != 1:
                d2[d1[nums[j]] - 1].remove(nums[j])

            j -= 1

        c = list(d2.keys())
        c.sort()

        r = []
        for i in c[::-1]:
            # len(r) < k and
            if len(r) == k:
                return r

            if len(r) + len(d2[i]) <= k:
                r += d2[i]
            else:
                r += d2[i][:k - len(r)]

        return r

    def other(self, nums, k):
        import collections
        import heapq
        count = collections.Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)


if __name__ == '__main__':
    s = Solution()
    r = s.topKFrequent([7, 8, 8, 9, 9, 9], 1)
    print(r)
