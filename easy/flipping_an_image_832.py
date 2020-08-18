# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意很好理解就是给定二维矩阵，根据要求将它水平翻转
操作一：
[1, 1, 0] -> [0, 1, 1]
操作二，0 -> 1, 异或操作
[0, 1, 1] -> [1, 0, 0]
"""


class FlippingAnImage(object):

    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        rows = len(A)
        columns = len(A[0])
        for i in range(rows):
            A[i] = A[i][::-1]
            for j in range(columns):
                A[i][j] ^= 1
        return A

