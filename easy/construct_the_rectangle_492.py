# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
import math
"""
Solutions:
解决这道题目的思路比较简单根据题目给我要求：1、2、3
那么我们可以想到最接近答案的理想情况就是正方形，就是面积的开方，
然后要求长大于等于宽的情况下，我们不断去增加边长即可。
"""


class ConstructTheRectangle(object):

    def constructRectangle(self, area):
        mid = int(math.sqrt(area))
        while mid > 0:
            if area % mid == 0:
                return [int(area / mid), int(mid)]
            mid -= 1

