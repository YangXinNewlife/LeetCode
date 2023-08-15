# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
判断给定范围的数据left和right之间确定都出现在ranges数组中至少一次
直接for循环遍历查找即可
"""


class CheckIfAllTheIntegersInARangeAreCovered(object):

    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for i in range(left, right + 1):
            result = 0
            for j in range(len(ranges)):
                if ranges[j][0] <= i <= ranges[j][1]:
                    result += 1
            if result == 0:
                return False
        return True
