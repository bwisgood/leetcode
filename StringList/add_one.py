class Solution:
    def plusOne(self, digits):
        return list(str(int("".join(list(map(str, digits)))) + 1))
