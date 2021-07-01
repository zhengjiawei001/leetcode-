# -*- coding: utf-8 -*-
# @Time    : 2021/7/1 9:47 上午
# @Author  : zhengjiawei
# @FileName: 数组中重复的数字.py
# @Software: PyCharm
"""
找出数组中重复的数字。

在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，
但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。


"""
from typing import *


class Solution:

    def findRepeatNumber(self, nums: List[int]) -> int:
        result_ = []
        for each in nums:
            if nums.count(each) > 1:
                result_.append(each)
        return result_[0]


class Solution_:
    """
    使用集合会减少内存消耗和执行时间，
    如果使用list的count功能，功能也能实现，但是时间复杂度比较高
    """
    def findRepeatNumber(self, nums: List[int]) -> int:
        result = set()
        for each in nums:
            if each in result:
                return each
            result.add(each)
        return -1


if __name__ == '__main__':
    s = Solution()
    result = s.findRepeatNumber([2, 3, 1, 0, 2, 5, 3])
    print(result)
