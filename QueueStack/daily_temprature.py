class Solution:
    def dailyTemperatures(self, T):
        stack = []
        answer = [0 for _ in range(len(T))]
        for i, e in enumerate(T):
            if stack:
                while stack and T[stack[-1]] < e:
                    answer[stack[-1]] = i - stack[-1]
                    stack.pop()
            stack.append(i)
        return answer


if __name__ == '__main__':
    solution = Solution()

    print(solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
