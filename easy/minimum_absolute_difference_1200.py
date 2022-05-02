# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
本题的含义是找出给出数组的每两个元素的差值组成的数组对。
逻辑是我们现根据遍历每个数字生成每两个的最小值和对应的数组对，
遇到更小的就清空返回结果，因为之前的数组差值已经比当前的最小值大了。
"""


class MinimumAbsoluteDifference(object):

    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        i = 1
        min_dis = float("inf")
        result = list()
        while i < len(arr):
            dis = arr[i] - arr[i - 1]
            if dis < min_dis:
                min_dis = dis
                result = [[arr[i - 1], arr[i]]]
            elif dis == min_dis:
                result.append([arr[i - 1], arr[i]])
            i += 1
        return result

