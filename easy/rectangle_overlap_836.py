# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
题目的含义就是给定两个矩阵的范围，我们根据范围来找范围点是否有交集，
例如我们确定一个矩阵不变，去判断另一个矩阵的点是否与现在的点之间有交集，我们先判断矩阵的四个方向（上、下、左、右）。
然后我们排除（左、右、上、下）的不重合位置，即为重合的情况（这里使用not来取反）；
"""


class RectangleOverlap(object):

    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        rec1_x1, rec1_y1, rec1_x2, rec1_y2 = rec1
        rec2_x1, rec2_y1, rec2_x2, rec2_y2 = rec2
        return not (rec1_x1 >= rec2_x2 or rec1_x2 <= rec2_x1 or rec1_y1 >= rec2_y2 or rec1_y2 <= rec2_y1)
