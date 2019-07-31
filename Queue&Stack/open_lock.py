class Solution:
    """
    You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

    The lock initially starts at '0000', a string representing the state of the 4 wheels.

    You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

    Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

    """

    def openLock(self, deadends, target: str) -> int:
        from queue import Queue
        from copy import deepcopy

        _START = '0000'
        # exclude wrong condition
        if _START in deadends or len(deadends) > 500:
            return -1

        if target == _START:
            return 0
        # resolve if the deadends is ['0010'] and target is '0019'
        tl = list(target)
        # 1. create a queue to store next numbers, and initialize the step equal 0
        q = Queue()
        q.put(_START)
        step = 0

        # 2. while current number exist & target number not found
        def next_number(cur_):
            iter_cur = deepcopy(cur_)
            for i, e in enumerate(cur_):
                if e != tl[i]:
                    temp = list(iter_cur)
                    if int(tl[i]) - int(e) > 5 or int(tl[i]) - int(e) < 0:
                        temp[i] = str(int(temp[i]) - 1)
                    else:
                        temp[i] = str(int(temp[i]) + 1)
                    s = "".join(temp)
                    if s in deadends:
                        continue
                    else:
                        return s
            return None

        while not q.empty():
            current = q.get()
            step += 1
            # 2.1 judge if current number is target number
            if current == target:
                return step
            # 3. add next possible number to the queue
            next_ = next_number(current)
            # cancel comment next line to check out the step
            # print(next_, end='->')
            if not next_:
                continue
            else:
                q.put(next_)
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.openLock(deadends=['1234'], target='0123'), 'step')
