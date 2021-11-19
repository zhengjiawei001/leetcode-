# -*- coding: utf-8 -*-
# @Time    : 2021/11/2 8:15 下午
# @Author  : zhengjiawei
# @FileName: xin1111.py
# @Software: PyCharm
# 求解sqrt(2)


# [0,1]
# def sqrt():
#     low = 1
#     high = 1.5
#     mid = (low+high)/2
#     while high-mid > 0.0001:
#         if mid*mid > 2:
#             high = mid
#         else:
#             low = mid
#         mid = (low+high)/2
#     return mid

# 山脉数组找最大值
a = [1, 2, 3, 5, 7, 9, 4, 2]


def sort(a):
    s = 0
    e = len(a)

    while s <= e:
        mid = (s + e) // 2
        if mid == s or mid == e - 1:
            return a[mid]

        if a[mid] >= a[mid - 1] and a[mid] >= a[mid + 1]:
            return a[mid]

        elif a[mid] < a[mid - 1]:
            e = mid - 1
        elif a[mid] > a[mid - 1]:
            s = mid
    return -1


print(sort(a))


