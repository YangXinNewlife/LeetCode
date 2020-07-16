# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意大概的意思就是A或者B中是否有经过多次顺序调换后，还和A或者B是一样的，
那么就得考虑一样的话元素长度得相同、然后还有还可以让 A + A, 再判断是否存在B就可以了；
"""


class RotateString(object):

    def rotateString(self, A: str, B: str) -> bool:
        return len(A) == len(B) and B in A + A

