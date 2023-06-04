# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的意思是给定一个标准点，x和y分别代表x轴和y轴。
然后给定一串点，如果这里有x或y相同的点，
计算相关的曼哈顿距离，找到最小点的下标并返回
曼哈顿距离：
abs(points[i][0] - x) + abs(points[i][1] - y)
"""


class FindNearestPointThatHasTheSameXOrYCoordinate(object):

    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        result = -1
        distance_max = float('inf')
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                dis = abs(points[i][0] - x) + abs(points[i][1] - y)
                if dis < distance_max:
                    distance_max = dis
                    result = i
        return result



