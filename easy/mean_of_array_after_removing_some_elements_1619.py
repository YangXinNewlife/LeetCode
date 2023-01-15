# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是根据给定的数组，然后去掉数组中最大的和最小的0.05个，
最后再计算下剩余的元素的平均数即可
单位保留浮点型
"""


class MeanOfArrayAfterRemovingSomeElements(object):

    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        remove_size = int(len(arr) * 0.05)
        rest_list = arr[remove_size: -remove_size]
        return float(sum(rest_list)) / len(rest_list)

