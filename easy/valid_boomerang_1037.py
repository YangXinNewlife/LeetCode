# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的意思是判断给定的三个点是否在一条线上。
判断三点是否共线，那么对于三个点 p1，p2，和 p3，
只要 p1 和 p2 连接而成的直线和 p1 和 p3 连接而成的直线重合，则表示三点共线。
只要满足 (y3 - y1) / (x3 - x1) = (y2 - y1) / (x2 - x1)，就表示三点共线，
换成乘法形式的就是 (y3 - y1) * (x2 - x1) = (y2 - y1) * (x3 - x1)
"""


class ValidBoomerang(object):

    def isBoomerang(self, points: List[List[int]]) -> bool:
        return (points[2][1] - points[0][1]) * (points[1][0] - points[0][0]) != (points[1][1] - points[0][1]) * (
                    points[2][0] - points[0][0])

