# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的含义就是去掉相邻的两个相同的小写字符
我们考虑用栈特性来实现
"""


class RemoveAllAdjacentDuplicatesInString(object):

    def removeDuplicates(self, s: str) -> str:
        stack = list()
        for i in s:
            if stack and i == stack[-1]:
                stack.pop()
                continue
            stack.append(i)
        return "".join(stack)

