# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solution:
题意是找到给定的坐标中两个宽度最大的（其实就是X轴或者横坐标距离最大的）。
这里直接取出来所有点的横坐标然后进行排期，直接判断最大的距离即可。
"""

class WidestVerticalAreaBetweenTwoPointsContainingNoPoints(object):

    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        point_x_list = sorted([point_x[0] for point_x in points])
        result = 0
        for i in range(1, len(point_x_list)):
            x = point_x_list[i] - point_x_list[i - 1]
            result = max(result, x)
        return result
