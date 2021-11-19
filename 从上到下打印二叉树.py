# -*- coding: utf-8 -*-
# @Time    : 2021/11/15 7:36 下午
# @Author  : zhengjiawei
# @FileName: 从上到下打印二叉树.py
# @Software: PyCharm

# 从上到下打印二叉树
# Definition for a binary tree node.
# 给定二叉树: [3,9,20,null,null,15,7],
# [3,9,20,15,7]

import collections
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 深度优先搜索
class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root: return []
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            res.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return res


# 2、给定[3,9,20,null,null,15,7],
# 输出 [
#   [3],
#   [9,20],
#   [15,7]
# ]
# 对于树的结构，中值只能通过node.val获取
class Solution1:
    def levelOrder(self, root: TreeNode) -> List[int]:
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append.append(node.right)
            res.append(tmp)
        return res


# 请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，
# 第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。
# 给定二叉树: [3,9,20,null,null,15,7]
# 输出[
#   [3],
#   [20,9],
#   [15,7]
# ]
class Solution2:
    def levelOrder(self, root: TreeNode) -> List[int]:
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            tmp = []
            for i in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:queue.append(node.left)
                if node.right:queue.append(node.right)
            res.append(tmp[::-1] if len(res) % 2 else tmp)
        return res


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def recur(A, B):
            if not B: return True
            if not A or A.val != B.val: return False
            return recur(A.left, B.left) and recur(A.right, B.right)

        return bool(A and B) and (recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))

