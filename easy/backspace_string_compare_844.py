# -*— coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意就是#代表删除按键，退格。
那么使用栈结构来处理即可
"""


class BackspaceStringCompare(object):

    def backspaceCompare(self, S: str, T: str) -> bool:
        stack_s, stack_t = list(), list()
        for i in S:
            if i != '#':
                stack_s.append(i)
            elif stack_s:
                stack_s.pop()
        for j in T:
            if j != '#':
                stack_t.append(j)
            elif stack_t:
                stack_t.pop()
        return stack_s == stack_t



