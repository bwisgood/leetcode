class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def str_sum(s):
            temp = list(map(int, s[::-1]))
            _sum = 0
            for i, e in enumerate(temp):
                _sum += (2 ** i) * e
            return _sum

        a_sum = str_sum(a)
        b_sum = str_sum(b)

        v = a_sum + b_sum

        def sum_str(i):
            s = ""
            while i:
                i, _s = divmod(i, 2)
                s += str(_s)
            return s[::-1]

        return sum_str(v) if v else "0"


if __name__ == '__main__':
    s = Solution()
    r = s.addBinary("0", "0")
    print(r)
