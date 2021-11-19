# -*- coding: utf-8 -*-
# @Time    : 2021/11/6 3:02 下午
# @Author  : zhengjiawei
# @FileName: 复制复杂链表.py
# @Software: PyCharm


# Definition for a Node.

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        temp_set = set()
        while head:
            if head in temp_set:
                return True
            temp_set.add(head)
            head = head.next

        return False

# class Solution:
#     def copyRandomList(self, head: 'Node') -> 'Node':
#         curr = head
#         prev = dum =  Node(0)


