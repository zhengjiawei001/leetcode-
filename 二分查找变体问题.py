# -*- coding: utf-8 -*-
# @Time    : 2021/11/11 2:21 下午
# @Author  : zhengjiawei
# @FileName: 二分查找变体问题.py
# @Software: PyCharm

# 查找第一个值等于给定值的元素
def search_num(a, value):
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = low + ((high - low) >> 2)
        if a[mid] > value:
            high = mid - 1
        elif a[mid] < value:
            low = mid + 1
        else:
            if mid == 0 or a[mid - 1] != value:
                return mid
            else:
                high = mid - 1
    return -1


# 查找最后一个值等于给定值的元素
def search_num1(a, value):
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if a[mid] > value:
            high = mid - 1
        elif a[mid] < value:
            low = mid + 1
        else:
            if mid == high or a[mid + 1] != value:
                return mid
            else:
                low = mid + 1


# 查找第一个值大于或等于给定值的元素
def search_num2(a, value):
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if a[mid] < value:
            low = mid + 1
        else:
            if mid == 0 or a[mid - 1] < value:
                return mid
            else:
                low = mid + 1
    return -1


# 查找最后一个值小于或等于给定值的元素
def search_num3(a, value):
    low, high = 0, len(a) - 1
    while low <= high:
        mid = low +((high-low)>>2)
        if a[mid] > value:
            high = mid -1
        else:
            if mid == 0 or a[mid+1] >value:
                return mid
            else:
                low = mid + 1
    return -1



