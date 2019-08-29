class Solution:
    def fourSumCount(self, A, B, C, D) -> int:
        from collections import Counter
        dic = Counter(a + b for a in A for b in B)
        return sum([dic[-c - d] for c in C for d in D])
        # h = Counter(-a - b for a in A for b in B)
        # return sum([h[c + d] for c in C for d in D])


if __name__ == '__main__':
    s = Solution()
    r = s.fourSumCount(A=[1, 2],
                       B=[-2, -1],
                       C=[-1, 2],
                       D=[0, 2],
                       )
    print(r)
