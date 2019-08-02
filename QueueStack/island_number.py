class Solution:
    def numIslands(self, grid) -> int:
        # 首先从第一行第一个元素开始遍历
        # 找到第一个值为1且不在已遍历列表的元素
        # `添加它的上下左右为1且不在已遍历set中的元素入栈
        # 从最后一个开始遍历栈中元素
        # 添加它的上下左右为1且不在已遍历set中的元素入栈
        # 重复上述操作`
        # 直到栈空为止
        # 让岛屿数量加一
        # 重复上述操作
        island = 0
        around = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        try:
            l = len(grid[0])
            h = len(grid)
        except (TypeError, IndexError):
            return 0

        def find_island(cur_, grid):
            x, y = cur_
            for a, b in around:
                a += x
                b += y
                if 0 <= a < h and 0 <= b < l and grid[a][b] == "1":
                    grid[a][b] = "0"
                    find_island((a, b), grid)

        for i in range(h):
            for j in range(l):
                cur = grid[i][j]
                if cur == "1":
                    grid[i][j] = "0"
                    find_island((i, j), grid)
                    island += 1
        return island


if __name__ == '__main__':
    solution = Solution()
    # solution.numIslands([
    #     ['1', '1', '0', '1', '0'],
    #     ['1', '0', '1', '1', '0'],
    #     ['1', '0', '1', '0', '0'],
    #     ['1', '0', '0', '1', '0'],
    #     ['1', '0', '1', '1', '0'],
    # ])
    print(solution.numIslands([]))
