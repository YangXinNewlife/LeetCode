# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
这道题不难，但是难的是理解题意。
首先目的是统计矩阵中有多少个奇数。
然后我们可以从二维的角度将行和列拆开算。
逻辑是现将给定的单位indices[i]，分别加1后，然后indices[i]所在的行和列也分别加1
这样例子的演进如下：
000 121 131
000 010 131
最后1和3都是奇数所以是6个。
"""


class CellsWithOddValuesInAMatrix(object):

    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row = [0] * m
        column = [0] * n
        for i, j in indices:
            row[i] += 1
            column[j] += 1

        row_cnt = column_cnt = 0
        for index in range(m):
            if row[index] % 2 == 1:
                row_cnt += 1

        for index in range(n):
            if column[index] % 2 == 1:
                column_cnt += 1
        return row_cnt * n + column_cnt * m - 2 * row_cnt * column_cnt

