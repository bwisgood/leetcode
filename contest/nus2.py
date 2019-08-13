class Solution:
    def minSwaps(self, data: list) -> int:
        one_times = data.count(1)
        b = one_times - 1
        temp_a = 0

        if one_times - 1 <= 0:
            return 0

        min_index = one_times - 1

        for i, j in enumerate(data):
            if data[i] == 0:
                temp_a += 1
        if temp_a < min_index:
            min_index = temp_a

        for a, e in enumerate(data):
            if len(data) - a - 1 < one_times:
                break
            temp = 0
            if data[a] != data[a + 1] and data[a] == 0:
                temp -= 1
            if data[b] != data[b + 1] and data[b] == 1:
                temp += 1
            temp_a += temp
            b += 1
            if temp_a < min_index:
                min_index = temp_a

        return min_index


if __name__ == '__main__':
    s = Solution()
    print(s.minSwaps([1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1]))
    print(s.minSwaps([1, 0, 1, 0, 1]))
    print(s.minSwaps([1, 1, 1, 0, 1]))
    print(s.minSwaps([1, 1, 1, 1, 1]))
    print(s.minSwaps([0, 0, 0, 0]))
    print(s.minSwaps([0, 1, 1, 0, 0]))
