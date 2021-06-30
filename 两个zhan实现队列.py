# -*- coding: utf-8 -*-
"""用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )
"""


class CQueue:

    def __init__(self):
        self.A, self.B = [], []

    def appendTail(self, value):
        self.A.append(value)

    def deleteHead(self):
        if self.B:
            return self.B.pop()
        if not self.A:
            return -1
        while self.A:
            self.B.append(self.A.pop())
        return self.B.pop()


class CQueue_:

    def __init__(self):
        self.A = []

    def appendTail(self, value):
        self.A.append(value)

    def deleteHead(self):
        if self.A:
            result = self.A[0]
            self.A = self.A[1:]
            return result
        if not self.A:
            return -1


if __name__ == '__main__':
    obj = CQueue()
    obj.appendTail(3)
    param_2 = obj.deleteHead()
    param_3 = obj.deleteHead()
    print(param_2, param_3)
