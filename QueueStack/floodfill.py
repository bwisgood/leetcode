class Solution:
    def floodFill(self, image: list, sr: int, sc: int, newColor: int) -> list:
        # bfs
        """
        初始化一个队列
        将当前的点位相邻的点加到队列中
        """
        from queue import Queue
        # if image[sc][sr] == 0:
        #     return image

        base_color = image[sr][sc]

        h = len(image)
        l = len(image[0])
        q = Queue()
        visited = set()
        q.put((sr, sc))
        around = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while not q.empty():
            sr, sc = q.get()
            image[sr][sc] = newColor
            for opt_r, opt_c in around:
                x = sr + opt_c
                y = sc + opt_r
                if 0 <= x < h and 0 <= y < l and image[x][y] == base_color and (x, y) not in visited:
                    visited.add((x, y))
                    q.put((x, y))
        return image


if __name__ == '__main__':
    from pprint import pprint

    s = Solution()
    a = s.floodFill([[0, 0, 0],
                     [0, 1, 0]], 1, 1, 2)

    pprint(a)

    a = s.floodFill([[0, 0, 0],
                     [1, 0, 0]], 1, 0, 2)
    from pprint import pprint

    pprint(a)
