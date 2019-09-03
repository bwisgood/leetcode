class ZeroEvenOdd:
    def __init__(self, n):
        from threading import Lock
        self.n = n
        self.mutex = Lock()
        self.num = 0
        self.times = 0
        from threading import Thread
        from concurrent.futures import ThreadPoolExecutor
        mp = {
            0: self.zero,
            1: self.even,
            2: self.odd
        }
        with ThreadPoolExecutor(3) as excutor:
            for i in range(n):
                excutor.submit(mp[i % 2], i)

    """
    01020304
    """

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber) -> None:
        with self.mutex:
            if self.times <= self.n * 2:
                # printNumber()
                print(0)

                self.times += 1

    def even(self, printNumber) -> None:
        with self.mutex:
            if self.num == 0:
                if self.times <= self.n * 2:
                    # printNumber()
                    print(2)
                    self.num = 1
                    self.times += 1

    def odd(self, printNumber) -> None:
        with self.mutex:
            if self.num == 1:
                if self.times <= self.n * 2:
                    # printNumber()
                    print(1)
                    self.num = 0
                    self.times += 1


if __name__ == '__main__':
    s = ZeroEvenOdd(10)
