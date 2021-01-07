# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的意思就是找到参数n的二进制表示中，最大两个1中的距离；
例如22 -> 10110, 第一个和第三个位置距离为2；
那么我们每次可以记录每个1的位置，以及和下一个1的距离差，我们最后返回最大的那个就好了；
"""


class BinaryGap(object):

    def binaryGap(self, n: int) -> int:
        binary = bin(n)[2:]
        dists = [0] * len(binary)
        left = 0
        for i, b in enumerate(binary):
            if b == '1':
                dists[i] = i - left
                left = i
        return max(dists)



