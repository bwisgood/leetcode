class Solution:
    def evalRPN(self, tokens) -> int:
        # 新建一个表达式,如果当前字符为变量或者为数字，则压栈，
        # 如果是运算符，则将栈顶两个元素弹出作相应运算，结果再入栈，
        # 最后当表达式扫描完后，栈里的就是结果。
        stack = []

        opt = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y)
        }

        for token in tokens:
            try:
                token = int(token)
            except ValueError:
                value1 = stack.pop()
                value2 = stack.pop()
                stack.append(opt.get(token)(value2, value1))
            else:
                stack.append(token)
        return stack[0]


if __name__ == '__main__':
    solution = Solution()
    solution.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
