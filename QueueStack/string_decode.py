class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        this_str = ''
        num = 0
        for i in s:
            if i.isdigit():
                num = num * 10 + int(i)
            elif i.isalpha():
                this_str += i
            elif i == '[':
                stack.append((this_str, num))
                this_str, num = '', 0
            else:
                last_str, this_num = stack.pop()
                this_str = last_str + this_num * this_str
        return this_str


if __name__ == '__main__':
    s = Solution()
    # print(s.decodeString("2[a]2[b2[c2[d]]e]f"))
    print(s.decodeString("2[2[a]b2[e]f]"))
    "aabeefaabeef"
    "aaabFFFFcbFFFFc"
    # print(s.decodeString("10[a]"))
    # "abcabccdcdcdef"
    # "abcabccdcdcdef"
