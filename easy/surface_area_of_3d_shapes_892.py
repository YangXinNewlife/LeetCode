# -*- codinh:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意：
跟之前的题目类似，这里就是给出多组数据，每个数值的含义就是有多少个 1 * 1 * 1 的正方形块，我们计算这堆数值（正方形块）组成的三维物体的面积

解题思路：
我们把这类问题拆分成几种情景：
1.只有一块，面积就是6；
2.只有一个柱子（多块叠加在一起），那么我们知道中间的块上与下的两面是要叠加在一起的，所以说一个柱子（多个块叠加的）面积就是 n * 4 + 2
3.多个柱子，就是有左右两侧也有重叠的部分，我们判断重叠的高度，选取两者最小的就是重叠的部分 min * 2;
这样我们通过三组公式可以计算出来面积如下代码。
"""


class SurfaceAreaOf3DShapes(object):

    def surfaceArea(self, grid: List[List[int]]) -> int:
        result = 0
        grid_n = len(grid)
        for i in range(grid_n):
            for j in range(grid_n):
                if grid[i][j]:
                    result += grid[i][j] * 4 + 2
                if i:
                    result -= min(grid[i][j], grid[i - 1][j]) * 2
                if j:
                    result -= min(grid[i][j], grid[i][j - 1]) * 2
        return result
