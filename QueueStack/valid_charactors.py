class Solution:
    def isValid(self, s: str) -> bool:
        match = {
            "(": ")",
            "{": "}",
            "[": "]",
            ")": "(",
            "}": "{",
            "]": "[",
        }
        stack = []
        for i in s:
            if not len(stack):
                stack.append(i)
                continue
            if stack[-1] != match.get(i):
                stack.append(i)
            else:
                stack.pop()
        if len(stack):
            return False
        else:
            return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isValid("{[({(){}[])})]}"))
