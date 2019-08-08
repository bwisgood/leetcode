class Solution:
    def canVisitAllRooms(self, rooms) -> bool:
        # 获取房间数量
        # 创建一个长度为房间数量的列表均为0
        # 开始进入房间
        # 取出所有房间内的钥匙入栈
        # 从栈中获取房间号如果已经去过了则跳过，如果没去过则取出里面的钥匙入栈
        rooms_num = len(rooms)
        visited = set()
        rooms_state = [0 for _ in range(rooms_num)]

        stack = [0]
        while stack:
            c = stack.pop()
            visited.add(c)
            rooms_state[c] = 1
            keys = rooms[c]
            for key in keys:
                if key not in visited:
                    stack.append(key)

        return False if 0 in rooms_state else True

    def another(self, rooms):
        # 创建一个set
        # 遍历每个房间取钥匙，但是不能取当前自己房间的钥匙
        # add到set中
        # 最终判断钥匙数量和房间数量是否相等即可
        keys = set()
        keys.add(0)
        for i, e in enumerate(rooms):
            if e:
                for k in e:
                    if k != i:
                        keys.add(k)
        return True if len(keys) == len(rooms) else False


if __name__ == '__main__':
    s = Solution()
    c = s.another([[1], [2], [3], []])
    print(c)
