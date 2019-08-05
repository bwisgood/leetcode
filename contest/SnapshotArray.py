class SnapshotArray:

    def __init__(self, length: int):
        self.l = [0 for _ in range(length)]
        self.d = {}
        self.snap_num = 0
        self.buffer = []
        self.has_changed = set()

    def set(self, index: int, val: int) -> None:
        self.buffer.append((index, val))
        self.has_changed.add(index)
        self.l[index] = val

    def snap(self) -> int:
        self.snap_num += 1
        snap_id = self.snap_num - 1
        from copy import deepcopy
        self.d[snap_id] = deepcopy(self.buffer)
        self.buffer = []
        return snap_id

    def get(self, index: int, snap_id: int) -> int:
        if index not in self.has_changed:
            return self.l[index]

        for i in range(snap_id + 1):
            c = self.d.get(i)
            for k, v in reversed(c):
                if k == index:
                    return v


# Your SnapshotArray object will be instantiated and called as such:
obj = SnapshotArray(3)
obj.set(0, 5)
obj.set(0, 9)
obj.set(0, 13)
param_2 = obj.snap()
param_3 = obj.get(0, 0)

print(param_2)
print(param_3)
