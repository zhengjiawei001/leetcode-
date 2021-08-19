# -*- coding: utf-8 -*-
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head):
        return self.merge_sort(head)

    def merge_sort(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head

        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None  # 从中间截断

        L = self.merge_sort(head)
        R = self.merge_sort(head2)
        return self.merge(L, R)

    def merge(self, L: ListNode, R: ListNode) -> ListNode:
        dummy = ListNode(-1)  # 创建哑结点
        x = dummy
        while L and R:
            if L.val < R.val:
                x.next = L
                L = L.next
            else:
                x.next = R
                R = R.next
            x = x.next
        if L:
            x.next = L
        if R:
            x.next = R
        return dummy.next


heads = [4, 2, 1, 3]
dummy = ListNode(-1)
head = dummy
for i in heads:
    node = ListNode(i)
    head.next = node
    head = head.next

head = dummy.next

while head:
    print(head.val)
    head = head.next
