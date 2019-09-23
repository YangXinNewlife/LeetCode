# -*- coding:utf-8 -*-
__author__ = 'yangxin'
"""
Solutions:
这里的办法很简单，首先我们要知道一个island周长是4（上、下、左、右）。
然后我们去判断每个island的四周是否有island，有的话周长就减去1。
"""


class IslandPerimeter(object):

    def islandPerimeter(self, grid):
        """
        :param grid:
        :return:
        """
        perimeter = 0
        grid_rows = len(grid)
        if grid_rows == 0:
            return 0
        grid_cols = len(grid[0])
        for i in range(grid_rows):
            for j in range(grid_cols):
                if grid[i][j] == 1:
                    perimeter += 4
                    if i > 0 and grid[i-1][j]:
                        perimeter -= 1
                    if j > 0 and grid[i][j-1]:
                        perimeter -= 1
                    if i + 1 < grid_rows and grid[i + 1][j]:
                        perimeter -= 1
                    if j + 1 < grid_cols and grid[i][j + 1]:
                        perimeter -= 1
        return perimeter

