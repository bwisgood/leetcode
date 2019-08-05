class Solution:
    def findTargetSumWays(self, nums, S) -> int:
        # node = (step, sum)
        # 不需要visited 会超时
        # nums中每多一个0，结果way = way * (zero_num**2)
        temp = nums[:]
        zero_sum = 0
        visited = set()
        # if zero_sum > 0:
        #     nums = list(set(nums))
        #     nums.remove(0)
        for i, e in enumerate(temp):
            if e == 0:
                zero_sum += 1
                # 不能用pop
                nums.remove(0)

        max = sum(nums)
        if max == S or -max == S:
            if zero_sum > 0:
                return 2 ** zero_sum
            else:
                return 1

        size = len(nums) - 1  # 4

        target = (size, S)
        way = 0
        stack = [(-1, 0)]
        # max_dict = {i: sum(nums[i:]) for i, e in enumerate(nums)}
        # print(max_dict)
        # 如果发现进行到某一步的时候后面的所有值相加加上当前的数都小于最终的结果那就跳过了
        # 或者发现进行到某一步的时候减去后面所有的值都大于当前的结果
        while stack:
            current = stack.pop()

            if current == target:
                way += 1
            if not current[0] < 0:
                c_max = sum(nums[current[0]:])
                if c_max and current[1] + c_max < S:
                    continue
                if c_max and current[1] - c_max > S:
                    continue
            for opt in (1, -1):
                if current[0] + 1 > size:
                    continue
                neighbor_step = current[0] + 1
                neighbor_sum = current[1] + opt * nums[current[0] + 1]
                neighbor = (neighbor_step, neighbor_sum)
                print(neighbor)
                if neighbor not in visited:
                    visited.add(neighbor)
                    if neighbor[1] == S:
                        way += 1
                    stack.append(neighbor)

        if zero_sum > 0:
            way = way * (2 ** zero_sum)
        return way

    def solve1(self, nums, S):
        d = {}
        length = len(nums)

        def dfs(i, cur, d):
            if i < length and (i, cur) not in d:  # 搜索周围节点
                d[(i, cur)] = dfs(i + 1, cur + nums[i], d) + dfs(i + 1, cur - nums[i], d)
            return d.get((i, cur), int(cur == S))

        return dfs(0, 0, d)


if __name__ == '__main__':
    s = Solution()
    print(s.findTargetSumWays([1, 1, 1, 1, 1], 3))
