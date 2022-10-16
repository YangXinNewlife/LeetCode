# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是给出一个矩阵，然后找出来有多少个负数，
其中处理逻辑因为是降序的，因此读每个列时可以按照逆序判断读取。
提高效率。
"""


class CountNegativeNumbersInASortedMatrix(object):

    def countNegatives(self, grid: List[List[int]]) -> int:
        result = 0
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col - 1, -1, -1):
                if grid[i][j] < 0:
                    result += 1
                else:
                    break
        return result

