# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意很简单，其实就是将n * m的矩阵根据要求做个是变幻。
其中变换步骤如下：
In one shift operation:
Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
正常来说就是向后挪移一个，如果是行末就是挪到下一行的第一个，如果是最后一行的最后一个
就挪到第一行的第一个，我们只需要判断三个位置即可。
"""


class Shift2DGrid(object):

    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        if k == 0:
            return grid
        m = len(grid)
        n = len(grid[0])
        for i in range(k):
            temp_grid = [[0] * n for i in range(m)]
            for j in range(m):
                for l in range(n):
                    if l != n - 1:
                        temp_grid[j][l + 1] = grid[j][l]
                    elif j != m - 1 and l == n - 1:
                        temp_grid[j + 1][0] = grid[j][l]
                    else:
                        temp_grid[0][0] = grid[j][l]
            grid = temp_grid
        return grid

