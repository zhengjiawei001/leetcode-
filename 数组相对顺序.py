# -*- coding: utf-8 -*-


# class Solution:
#     def relativeSortArray(self, arr1, arr2):
#         arr = []
#         for each in arr2:
#             pos = np.where(np.array(arr1) == each)[0]
#             if len(pos) > 1:
#                 arr.extend([arr1[i] for i in pos])
#             else:
#                 arr.append(arr1[pos[0]])
#         arr += sorted([each for each in arr1 if each not in arr])
#         return arr

# 思路简单，利用sorted 中key和lambda的结合
class Solution:
    def relativeSortArray(self, arr1, arr2):
        not_exist = [x for x in arr1 if x not in arr2]
        arr1 = [x for x in arr1 if x in arr2]
        return sorted(arr1, key=lambda num: arr2.index(num)) + sorted(not_exist)

# 最节约内存
class Solution:
    def relativeSortArray(self, arr1, arr2):
        ans = []
        while arr2:
            va = arr2.pop(0)
            while va in arr1:
                arr1.remove(va)
                ans.append(va)
        return ans + sorted(arr1)


if __name__ == '__main__':
    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]
    solution = Solution()
    result = solution.relativeSortArray(arr1, arr2)
    print(result)

