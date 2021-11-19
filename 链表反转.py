# -*- coding: utf-8 -*-
# @Time    : 2021/10/25 8:03 下午
# @Author  : zhengjiawei
# @FileName: 链表反转.py
# @Software: PyCharm


# 长度为n 数组arr
# m 左半段和右半段均为生序数组

# def quick_sort1(arr, m, p = 0, r):
#     def partition(data, p, r):
#         pivot_idx = m
#         data[pivot_idx], data[r - 1] = data[r - 1], data[pivot_idx]
#         i = p
#         for j in range(p, r):
#             if data[j] <= data[r - 1]:
#                 data[j], data[i] = data[i], data[j]
#                 i += 1
#         return i - 1
#
#     if r - p > 1:
#         q = partition(arr, p, r)
#         quick_sort1(arr, p, q)
#         quick_sort1(arr, q, r)


# def sort_merge(arr, m):
#     arr1 = []
#     i = 0
#     n = len(arr)
#     min_n = min(n - m, m)
#     j = m + 1
#     while i <= min_n:
#         if arr[i] < arr[j]:
#             arr1.append(arr[i])
#             i += 1
#         elif arr[i] >= arr[j]:
#             arr1.append(arr[j])
#             j += 1
#
#     return arr1


def reverseList(head):
    cur, prev = head, None
    while cur:
        cur.next, prev, cur = prev, cur, cur.next
    return prev
