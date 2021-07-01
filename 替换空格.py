# -*- coding: utf-8 -*-
# @Time    : 2021/7/1 10:22 上午
# @Author  : zhengjiawei
# @FileName: 替换空格.py
# @Software: PyCharm
"""请实现一个函数，把字符串 s 中的每个空格替换成"%20"。"""


class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(' ', '20%')


if __name__ == '__main__':
    s = Solution()
    print(s.replaceSpace("We are happy."))
