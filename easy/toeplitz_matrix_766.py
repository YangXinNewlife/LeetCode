# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意很简单，就是判断一个矩阵是不是托普利茨矩阵，
然后满足的条件就是矩阵的每一个元素的左上角与右下角，
即 (i,j) 坐标与 （i + 1, j + 1）坐标的元素是否相同即可；
"""


class ToeplitzMatrix(object):

    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix) - 1):
            for j in range(len(matrix[0]) - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True
