# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的意思就是name是想要输入的内容，但是typed代表实际输入的内容，我们输入的时候如果长按键盘会重复回复输入一些，
这时候我们既判断是否位一个字符即可。
"""


class LongPressedName(object):

    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j - 1]:
                j += 1
            else:
                return False
        return i == len(name)
