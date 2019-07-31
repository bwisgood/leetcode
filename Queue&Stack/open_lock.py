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

        _START = [0, 0, 0, 0]
        # exclude wrong condition
        if "".join(list(map(str, list(_START)))) in deadends or len(deadends) > 500:
            return -1

        # resolve if the deadends is ['0010'] and target is '0019'
        tl = list(map(int, list(target)))
        if tl == _START:
            return 0
        # 1. create a queue to store next numbers, and initialize the step equal 0
        q = Queue()
        q.put(_START)
        step = -1

        # if we need lend other numbers to transform current numbers we can store lend number's index
        self._LEND = -1

        # 2. while current number exist & target number not found
        def next_number(self, cur_):
            unequal_number_index = []
            # usual
            for i, e in enumerate(cur_):
                if e != tl[i]:
                    unequal_number_index.append(i)
                    if i == self._LEND:
                        continue
                    # to ensure the value in 0 - 9
                    temp_cur = deepcopy(cur_)
                    if tl[i] - e > 5 or tl[i] - e < 0:
                        value = temp_cur[i] - 1
                        if value < 0:
                            value = 9
                        temp_cur[i] = value
                    else:
                        temp_cur[i] = (temp_cur[i] + 1) % 10

                    if "".join(list(map(str, temp_cur))) in deadends:
                        continue
                    else:
                        return temp_cur

            # check if _LEND is surplus let the _LEND to -1 and return next_number(cur_)
            if len(unequal_number_index) == 1:
                if self._LEND >= 0 and self._LEND in unequal_number_index:
                    self._LEND = -1
                    return next_number(self, cur_)
            # lend a number form others
            if self._LEND >= 0:
                return None
            for i, e in enumerate(cur_):
                lend_cur = deepcopy(cur_)
                lend_cur[i] = (e + 1) % 10
                if "".join(list(map(str, lend_cur))) not in deadends:
                    self._LEND = i
                    return lend_cur
                lend_cur = deepcopy(cur_)
                temp = e - 1
                if e - 1 < 0:
                    temp = 9
                lend_cur[i] = temp
                if "".join(list(map(str, lend_cur))) not in deadends:
                    self._LEND = i
                    return lend_cur

            return None

        while not q.empty():
            current = q.get()
            step += 1
            # 2.1 judge if current number is target number
            if current == tl:
                return step
            # 3. add next possible number to the queue
            next_ = next_number(self, current)
            # cancel comment next line to check out the step
            print(next_, end='->')
            if not next_:
                continue
            else:
                q.put(next_)
        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.openLock(deadends=["0033","3201","0321","0122","3032","2120","1230","2303","2111","2030"], target="0123"),
          'step')
