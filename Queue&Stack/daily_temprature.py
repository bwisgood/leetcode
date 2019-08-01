class Solution:
    def dailyTemperatures(self, T):
        stack = T[:]
        answer = []

        for i in stack:
            T.pop(0)
            temp = []
            for j in T:
                if j > i:
                    answer.append(len(temp) + 1)
                    break
                else:
                    temp.append(j)
            if len(temp) == len(T):
                answer.append(0)
        return answer


if __name__ == '__main__':
    solution = Solution()
    print(solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
