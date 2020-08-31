# -*- coding:utf-8 -*-
__author__ = 'yangxin'
"""
Solutions:
题意就是找出满足如下，行、列、斜三个方向的和相等 = 15的结构
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.
因为是三阶，一共九8中组合，那么我们先用将每种可能写出来，然后我们根据以 5 为中心构建 
[grid[i - 1][j], grid[i - 1][j + 1], grid[i][j + 1], grid[i + 1][j + 1], grid[i + 1][j], grid[i + 1][j - 1], grid[i][j - 1], grid[i - 1][j - 1]]
逆时针结构，我们只需要判断给定的输入，并且拼接的结构在可能的其中，既是一种结果，我们判断其中有多少个结果即可；

"""


class MagicSquaresInGrid(object):

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        res, n = 0, len(grid)
        isMag = ['16729438', '18349276', '34927618', '38167294', '72943816', '76183492', '92761834', '94381672']
        for i in range(1, n - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 5:
                    tmp = ''.join(map(str, [grid[i - 1][j], grid[i - 1][j + 1], grid[i][j + 1], grid[i + 1][j + 1],
                                            grid[i + 1][j],
                                            grid[i + 1][j - 1], grid[i][j - 1], grid[i - 1][j - 1]]))
                    res += 1 if tmp in isMag else 0
        return res
