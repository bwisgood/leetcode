class Solution:
    def twoSum(self, numbers: list, target: int) -> list:
        i = 0
        j = len(numbers) - 1
        while i < j:
            sum_ = numbers[i] + numbers[j]
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            elif sum_ < target:
                i += 1
            else:
                j -= 1


if __name__ == '__main__':
    s = Solution()
    r = s.twoSum([1, 2, 3, 4], 3)
    print(r)
