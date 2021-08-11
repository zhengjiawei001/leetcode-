# -*- coding: utf-8 -*-
import random


# 非原地排序
def quick_sort(data):
    """快速排序"""
    if len(data) >= 2:
        # mid可以取任何数，但是如果取第一个数的时候，假设数据本身就是从小到大排列的
        # 那么快排的时间复杂度会退化到o(n*2),相同的，取最后一个数也是这样的，容易产生退化
        # 所以建议随机取
        mid = random.choice(data)
        left = []
        right = []
        for num in data:
            if num >= mid:
                right.append(num)
            else:
                left.append(num)
        return quick_sort(left) + [mid] + quick_sort(right)
    else:
        return data


def quick_sort1(data, p, r):
    def partition(data, p, r):
        pivot_idx = random.randint(p, r - 1)
        data[pivot_idx], data[r - 1] = data[r - 1], data[pivot_idx]
        i = p
        for j in range(p, r):
            if data[j] <= data[r - 1]:
                data[j], data[i] = data[i], data[j]
                i += 1
        return i - 1

    if r - p > 1:
        q = partition(data, p, r)
        quick_sort1(data, p, q)
        quick_sort1(data, q, r)


def merge_sort(items, comp=lambda x, y: x <= y):
    """归并排序"""
    if len(items) < 2:
        return items[:]
    mid = len(items) // 2
    left = merge_sort(items[:mid], comp)
    right = merge_sort(items[mid:], comp)
    return merge(left, right, comp)


def merge(items1, items2, comp):
    """合并(将两个有序的列表合并成一个有序的列表)"""
    pass


if __name__ == '__main__':
    data = [11, 8, 3, 9, 7, 1, 2, 5]
    quick_sort1(data, 0, len(data))
    print(data)
