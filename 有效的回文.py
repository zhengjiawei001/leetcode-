# -*- coding: utf-8 -*-
# @Time    : 2021/8/26 7:49 下午
# @Author  : zhengjiawei
# @FileName: 有效的回文.py
# @Software: PyCharm

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s0 = [each for each in s if each.isalnum()]
        s1 = ''.join(s0)
        s2 = ''.join(s0[::-1])
        return s1 == s2


class Solution1:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s0 = [each for each in s if each.isalnum()]
        n = len(s0)
        l = 0
        r = n - 1
        while l < r:
            if s0[l] != s0[r]:
                return False
            l += 1
            r -= 1
        return True


