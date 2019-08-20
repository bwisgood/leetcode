class Solution:
    def findRestaurant(self, list1: list, list2: list) -> list:
        map1 = {list1[i]: i for i in range(len(list1))}  # 转换hash
        map2 = {list2[i]: i for i in range(len(list2))}  # 转换hash
        inter = set(list1) & set(list2)  # 求交集
        sum_index = {i: map1[i] + map2[i] for i in inter}  # 交集成员索引求和
        return [val for val in inter if sum_index[val] == min(sum_index.values())]  # 找最少的索引和的成员
