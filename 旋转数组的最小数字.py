# -*- coding: utf-8 -*-
# @Time    : 2021/10/19 11:52 上午
# @Author  : zhengjiawei
# @FileName: 旋转数组的最小数字.py
# @Software: PyCharm
# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
# 输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
# 例如，数组[3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。
# 输入：[2,2,2,0,1]
# 输出：0

# 目的还是找数组中的最小值，可以使用二分法
from typing import List


#
#
# class Solution:
#     def minArray(self, numbers: List[int]) -> int:
#         # 使用双指针
#         low, high = 0, len(numbers) - 1
#         while low <= high:
#             mid = low + (high - low) // 2
#             if numbers[mid] < numbers[high]:
#                 high = mid
#             elif numbers[mid] > numbers[high]:
#                 low = mid + 1
#             else:
#                 high -= 1
#         return numbers[low]
#
#
# if __name__ == '__main__':
#     solution = Solution()
#     result = solution.minArray([2, 2, 2, 0, 1])
#     print(result)


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        return self.minArrayinter(numbers, 0, len(numbers) - 1)

    def minArrayinter(self, a, low, high):
        mid = low + ((high - low) >> 1)
        if a[mid] == a[high]:
            return self.minArrayinter(a, low, high - 1)
        if a[mid] < a[high]:
            return self.minArrayinter(a, low, mid - 1)

        if a[mid] > a[high]:
            return self.minArrayinter(a, mid + 1, high)


if __name__ == '__main__':
    solution = Solution()
    result = solution.minArray([2, 2, 2, 0, 1])
    print(result)
