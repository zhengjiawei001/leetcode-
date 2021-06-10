# -*- coding: utf-8 -*-

class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        len_0 = []
        len_1 = []
        for each in s.split('1'):
            len_0.append(len(each))

        for each in s.split('0'):
            len_1.append(len(each))

        return max(len_0) < max(len_1)


#
#
# class Solution_1:
#     def checkZeroOnes(self, s: str) -> bool:
#         max_0, max_1 = 0, 0
#         count_sum = 0
#         pre = '#'  # 上个字符
#         for each in s:
#             if pre == each:
#                 # 当前字符与上个字符相等
#                 count_sum += 1
#             # 当前字符与上个字符不相等
#             else:
#                 if pre == '0':
#                     max_0 = max(max_0, count_sum)
#                 if pre == '1':
#                     max_1 = max(max_1, count_sum)
#                 count_sum = 1
#             pre = each
#         # 字符串结尾的连续字串
#         if pre == '0':
#             max_0 = max(max_0, count_sum)
#         elif pre == '1':
#             max_1 = max(max_1, count_sum)
#         return max_1 > max_0


if __name__ == '__main__':
    solution = Solution()
    s = "1101"
    print(solution.checkZeroOnes(s))
