class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keys = []
        self.values = []

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        if key not in self.keys:
            self.keys.append(key)
            self.values.append(value)
        else:
            index = self.keys.index(key)
            self.values[index] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key not in self.keys:
            return -1

        index = self.keys.index(key)
        return self.values[index]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """

        if key not in self.keys:
            return
        index = self.keys.index(key)
        del self.keys[index]
        del self.values[index]


# Your MyHashMap object will be instantiated and called as such:
if __name__ == '__main__':
    obj = MyHashMap()
    obj.put(1, 1)
    obj.put(2, 2)
    param_2 = obj.get(1)
    obj.put(1, 3)
    param_3 = obj.get(1)
    obj.remove(1)
    print(obj.keys)
    print(obj.values)
