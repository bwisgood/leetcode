class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []
        self.top = None

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if self.empty():
            self.q.append(x)
            self.top = x
        else:
            self.q.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        t = self.q.pop(0)
        if self.q:
            self.top = self.q[0]

        return t

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.top

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.q == []


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
