# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的意思是要我们计算出来给定三个点的三角形形成的面积。
那么我们就得找一个公式，这里是用的是海伦公式，计算点组成的三角形的面积；
开始有一堆理论推导 -> s= 1/2 * abs(x1 * y2 + x2 * y3 + x3 * y1 - y1 * x2 - y2 * x3 - y3 * x1) 哈哈哈是不是很简单，想了解公式推导步骤请自行查询；
那么我们就缺少所有数据的组合可能性的排列组合。
这里我们使用Python的itertools.combinations方法生成排列组合；
"""

import itertools


class LargestTriangleArea(object):

    def largestTriangleArea(self, points: List[List[int]]) -> float:
        return max(0.5 * abs((y1 - x1) * (z2 - x2) - (z1 - x1) * (y2 - x2)) for (x1, x2), (y1, y2), (z1, z2) in itertools.combinations(points, 3))





