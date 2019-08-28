class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        s = set(J)
        n = 0
        for i in S:
            if i in s:
                n += 1
        return n
