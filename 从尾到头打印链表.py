# -*- coding: utf-8 -*-
from typing import *


# from Cython.Compiler.ExprNodes import ListNode


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        result = []
        while head:
            result.insert(0, head.val)
            head = head.next
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.reversePrint([1, 3, 2]))
