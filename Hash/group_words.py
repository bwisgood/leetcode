class Solution:
    def groupAnagrams(self, strs: list) -> list:
        def cal(str_):
            # list(str_).sort()
            c = list(str_)
            c.sort()
            return "".join(c)

        c = list(map(cal, strs))
        d = {}
        for i in range(len(c)):
            if c[i] in d:
                d[c[i]].append(i)
            else:
                d[c[i]] = [i]
        base = []
        for k, v in d.items():
            temp = []
            for index in v:
                temp.append(strs[index])
            base.append(temp)
        return base


if __name__ == '__main__':
    s = Solution()
    r = s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(r)
