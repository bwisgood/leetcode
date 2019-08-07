class Solution:
    def decodeString(self, s: str) -> str:
        # 初始化字符串""
        # 遇到"["就入栈等待处理
        # length = len(s)
        # cur = (0, s[0])
        if not s:
            return ""
        times_stack = []
        string_stack = []

        """
        for i in s:
            如果i是数字则说明他后面的字符需要翻倍i次
            如果是字符则需要加上之前的字符代表即将需要翻倍的字符
            如果是【 则表示即将开始记录需要翻倍的字符
            如果是】 则找到上一个【之后的所有字符和上一个需要翻倍的次数去做计算
            3[ab3[ab3[ab]]]
            3[ab]2[ab]
            2
            ababab ab
        """
        base = ""
        base_num = ""
        last_c = ""
        for i in s:
            if i.isnumeric():
                # times_stack.append(int(i))
                base_num += i
            elif i == "[":
                # if len(string_stack) != len(times_stack):
                if base != "":
                    string_stack.append(base)
                if base_num:
                    times_stack.append(int(base_num))
                base = ""
                base_num = ""
                last_c = "["
            elif i == "]":
                # 开始计算
                time = times_stack.pop()
                # ms = string_stack.pop()
                if base and last_c == "[":
                    t = time * base
                elif base and last_c == "]":
                    t = time * (string_stack.pop() + base)
                else:
                    t = time * string_stack.pop()
                if string_stack:
                    bt = string_stack.pop()
                    string_stack.append(bt + t)
                else:
                    string_stack.append(t)
                base = ""
                base_num = ""
                last_c = "]"
            else:
                base += i
        return "".join(string_stack) + base


if __name__ == '__main__':
    s = Solution()
    # print(s.decodeString("2[a]2[b2[c2[d]]e]f"))
    print(s.decodeString("2[2[a]b2[e]f]"))
    "aabeefaabeef"
    "aaabFFFFcbFFFFc"
    # print(s.decodeString("10[a]"))
    # "abcabccdcdcdef"
    # "abcabccdcdcdef"
