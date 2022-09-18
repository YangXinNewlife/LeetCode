# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目计算给定多个点的距离，因为每次可以移动水平、垂直、斜着三个方向，那么我们可以计算下：
1.两点共线：x_a == x_b or y_a == y_b 则 result += dis_x + dis_y
2.两点不共线则 result += max(dis_x, dis_y)
"""


class MinimumTimeVisitingAllPoints(object):

    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        result = 0
        if len(points) == 1:
            return result
        for i in range(1, len(points)):
            x_a, y_a = points[i - 1][0], points[i - 1][1]
            x_b, y_b = points[i][0], points[i][1]
            dis_x = abs(x_a - x_b)
            dis_y = abs(y_a - y_b)
            if x_a == x_b or y_a == y_b:
                result += dis_x + dis_y
            else:
                result += max(dis_x, dis_y)
        return result
