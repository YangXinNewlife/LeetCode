# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Soultions:
需要时间复杂度在O(n)常量级别。
方法一、用空间换时间：（下面代码中的方法）
我们设置两组List,分别存储数据以及对应当前的最小值。
然后一次去更新即可stack以及mins。

方法二、用一个变量去保存min_val最小值。
然后每次操作时，去要遍历所有元素去对比最小值。
"""


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.mins = []

    def push(self, x: int) -> None:
        """
        压栈/入栈
        :param x:
        :return:
        """
        min_val = self.getMin()
        if min_val is None or min_val > x:
            min_val = x
        self.mins.append(min_val)
        self.stack.append(x)

    def pop(self) -> None:
        """
        出栈/弹栈
        :return:
        """
        self.mins.pop()
        return self.stack.pop()

    def top(self) -> int:
        """
        获取栈中栈顶的元素
        :return:
        """
        return self.stack[-1]

    def getMin(self) -> int:
        """
        获取最小的元素
        :return:
        """
        if len(self.mins) == 0:
            return None
        return self.mins[-1]
