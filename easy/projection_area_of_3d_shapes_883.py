# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
首先要理解题意，题目的意思是给定一个二维数组，分别代表1 * 1 * 1矩阵的高，就是多少个小块累加一起。
那么我们要计算三个角度的阴影长度最大的和，那么我们需要分别算三个方向。
xy下方，下方就直接计算有几个高度就是几；
yz前方，求长度的最大值；
zx侧方，求长度的最大值即可；
"""


class ProjectionAreaOf3DShapes(object):

    def projectionArea(self, grid: List[List[int]]) -> int:
        top_result, front_result, side_result = 0, 0, 0
        n = len(grid)
        for i in range(n):
            x, y = 0, 0
            for j in range(n):
                if grid[i][j] != 0:
                    top_result += 1
                x = max(x, grid[i][j])
                y = max(y, grid[j][i])
            front_result += x
            side_result += y
        return top_result + front_result + side_result

