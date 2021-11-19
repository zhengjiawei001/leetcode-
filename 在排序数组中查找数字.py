# -*- coding: utf-8 -*-
# @Time    : 2021/11/9 11:07 上午
# @Author  : zhengjiawei
# @FileName: 在排序数组中查找数字.py
# @Software: PyCharm
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 虽然是二分法，不能直接找目标值，而是要找左边界和右边界
        i, j = 0, len(nums) - 1
        # 先搜索右边界
        while i <= j:
            m = (i + j) // 2

            if nums[m] <= target:  # 右边界在【m+1,j】这个区间
                i = m + 1
            else:
                j = m - 1  # 右边界在【i,m-1】这个区间
        right = i
        if j >= 0 and nums[j] != target:
            return 0

        # 搜索左边界
        i = 0
        while i <= j:
            m = (i + j) // 2
            if nums[m] < target:
                i = m + 1
            else:
                j = m - 1
        left = j
        return right - left - 1


if __name__ == '__main__':
    nums = [5,7,7,8,8,10]
    target = 8
    solution = Solution()
    result = solution.search(nums,target)
    print(result)