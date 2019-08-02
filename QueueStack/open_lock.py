class Solution:
    """
    You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

    The lock initially starts at '0000', a string representing the state of the 4 wheels.

    You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

    Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

    """

    def openLock(self, deadends, target: str) -> int:
        from queue import Queue
        # reduce query time
        deadends = set(deadends)
        _START = "0000"
        if _START in deadends:
            return -1
        q = Queue()
        q.put(_START)

        step = -1
        while not q.empty():
            step += 1
            for size in range(q.qsize()):
                current = q.get()
                print(current)
                if current == target:
                    return step

                for i in range(4):
                    if int(target[i]) - int(current[i]) > 5 or int(target[i]) < int(current[i]):
                        opt = -1
                    else:
                        opt = 1
                    # for add in opt:
                    next_ = list(current)
                    next_[i] = str((int(next_[i]) + opt) % 10)
                    next_ = "".join(next_)
                    if next_ not in deadends:
                        q.put(next_)
                        deadends.add(next_)
        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.openLock(deadends=["0033", "3201", "0321", "0122", "3032", "2120", "1230", "2303", "2111", "2030"],
                            target="0123"),
          'step')
