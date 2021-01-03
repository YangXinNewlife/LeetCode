# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
基本思路是矩阵的转置思想，行变列，元素对应赋值即可；
"""


class TransposeMatrix(object):

    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        row_size, col_size = len(A), len(A[0])
        result = [[0] * row_size for i in range(col_size)]
        for i in range(row_size):
            for j in range(col_size):
                result[j][i] = A[i][j]
        return result


