# -*- coding: utf-8 -*-
# @Time    : 2021/8/20 7:16 下午
# @Author  : zhengjiawei
# @FileName: 重排链表.py
# @Software: PyCharm


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None:
            return

            # -------- 先找中点
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow  # 中间或者中间偏左

        # -------- 右半段，翻转
        r_head = mid.next
        mid.next = None  # 左和右切断
        pre = None
        cur = r_head

        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        reverse_r_head = pre

        # -------- 两段拼接
        l = head
        r = reverse_r_head
        while r:
            l_nxt = l.next
            r_nxt = r.next

            r.next = l.next
            l.next = r

            l = l_nxt
            r = r_nxt


class Solution1:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None:
            return

        vec = []
        p = head
        while p:
            vec.append(p)
            p = p.next

        n = len(vec)
        l = 0
        r = n - 1
        while l < r:
            vec[r].next = vec[l].next
            vec[l].next = vec[r]
            l += 1
            r -= 1

        vec[l].next = None


if __name__ == '__main__':
    heads = [1, 2, 3, 4]
    dummy = ListNode(-1)
    head = dummy
    for i in heads:
        node = ListNode(i)
        head.next = node
        head = head.next

    head = dummy.next
    solution = Solution1()
    solution.reorderList(head)
    while head:
        print(head.val)
        head = head.next
