# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是找出给定数据集最大的n中有多少组满足如下特点：
a + b > c
a^2 + b^2 = c^2
直接遍历并套用公式即可
"""


class CountSquareSumTriples(object):

    def countTriples(self, n: int) -> int:
        result = 0
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                for k in range(j + 1, n + 1):
                    if i + j > k and i * i + j * j == k * k:
                        result += 1
        return result * 2
