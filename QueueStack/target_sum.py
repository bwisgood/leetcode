class Solution:
    def findTargetSumWays(self, nums, S) -> int:
        visited = set()
        size = len(nums) - 1

        target = (size, S)
        way = 0

        def find_way(current, target, visited, way, sum):
            c_index, c_value = current
            t_index, t_value = target

            if c_index + 1 > size:
                return
            # next = {"index": current["index"] + 1, "value": nums[current["index"] + 1]}
            next = (c_index + 1, nums[c_index + 1])
            for i in (1, -1):
                sum = c_value + nums[c_index + 1] * i
                if c_index == t_index and sum == t_value:
                    way += 1
                if (c_index, sum) not in visited:
                    visited.add(next)
                    find_way(next, target, visited, way, sum)

        find_way((-1, 0), target, visited, way, sum=0)
        print(way)


if __name__ == '__main__':
    s = Solution()
    s.findTargetSumWays([1, 1, 1, 1, 1], 3)
