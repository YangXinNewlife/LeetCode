# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
solutions:
题意是给定盒子的数量和每个盒子的大小，然后在给定一个卡车的容积
返回可以选择的最大可能性的盒子之和。
其实就是boxTypes[0]中的数量之和等于truckSize即可，选最大的
贪心算法
"""


class MaximumUnitsOnATruck(object):

    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda i: i[1], reverse=True)
        result = 0
        for i in boxTypes:
            if truckSize <= i[0]:
                result += truckSize * i[1]
                break
            else:
                result += i[0] * i[1]
                truckSize -= i[0]
        return result

