class Solution:
    def movesToMakeZigzag(self, nums) -> int:
        # use bfs
        from queue import Queue
        from copy import deepcopy

        q = Queue()
        step = -1
        length = len(nums)
        # 1. 每次复制一个nums到next node
        # 2. or 添加下一个要减少的索引到queue
        q.put(nums)
        step1 = -1
        while not q.empty():
            # 增加步数
            step += 1
            for size in range(q.qsize()):
                current = q.get()
                # 满足条件就退出循环
                not_feed = 0
                for j in range(1, length - 1, 2):
                    if not current[j - 1] < current[j] > current[j + 1]:
                        not_feed = j
                        break
                    if j == length - 1:
                        return step
                for i in (1, -1):
                    temp = deepcopy(current)
                    temp[not_feed + i] -= 1
                    if not temp[not_feed + i] < 0:
                        q.put(temp)


if __name__ == '__main__':
    solution = Solution()
    c = solution.movesToMakeZigzag([0, 7, 4, 8, 0])
    print(c)
