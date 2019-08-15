class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_set = []

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.hash_set.append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.hash_set.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        try:
            self.hash_set.index(key)
        except ValueError:
            return False
        else:
            return True

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
