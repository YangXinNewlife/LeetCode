# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的意思其实是判断给定的点是否都在一条线上，
我们直接套用公式判断三个点是否在一条线上即可，我们可以先保留2个点，然后for遍历第三个点即可。
三点是否在一条线点公式就是判断斜率
if ((x2 - x1) * (y3 - y1) != (y2 - y1) * (x3 - x1))
"""


class CheckIfItIsAStraightLine(object):

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        x1 = coordinates[0][0]
        y1 = coordinates[0][1]
        x2 = coordinates[1][0]
        y2 = coordinates[1][1]
        for i in range(2, len(coordinates)):
            x3 = coordinates[i][0]
            y3 = coordinates[i][1]
            if (x2 - x1) * (y3 - y1) != (y2 - y1) * (x3 - x1):
                return False
        return True
