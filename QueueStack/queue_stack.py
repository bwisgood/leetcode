class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from queue import Queue
        self.stack = Queue()
        self._top = None

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self._top = x

        if self.empty():
            self.stack.put(x)
            return
        temp = []
        while not self.empty():
            # self.stack.put(x)
            temp.append(self.stack.get())
        # temp.reverse()
        self.stack.put(x)
        for i in temp:
            self.stack.put(i)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        r = self.stack.get()
        if not self.stack.empty():
            self._top = self.stack.get()
            self.push(self._top)
        else:
            self._top = None
        return r

    def top(self) -> int:
        """
        Get the top element.
        """
        return self._top

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.stack.empty()


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
print(obj.top())
print(obj.pop())
print(obj.top())
print(obj.pop())
print(obj.pop())

param_4 = obj.empty()
