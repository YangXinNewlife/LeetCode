# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是计算矩阵的斜角的和，
其实逻辑相对简单，就是分别计算斜角的元素，mat[i][i] + mat[i][row_size - i - 1]
然后再把重复计算的减去即可。mat[row_size//2][row_size//2]
"""


class MatrixDiagonalSum(object):

    def diagonalSum(self, mat: List[List[int]]) -> int:
        row_size = len(mat)
        result = 0
        for i in range(row_size):
            result += mat[i][i] + mat[i][row_size - i - 1]
        if row_size % 2 == 1:
            result -= mat[row_size//2][row_size//2]
        return result

