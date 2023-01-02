# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是判断字符串中是否有对应的模式，
是否有m长度，k个重复的。
其实是一个动态规划的/数据公式问题，
转换公式是：
arr[i: i + m] * k == arr[i: i + m * k]
"""


class DetectPatternOfLengthMRepeatedKOrMoreTimes(object):

    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        arr_len = len(arr)
        for i in range(arr_len - m):
            if i + m * k <= arr_len and arr[i: i + m] * k == arr[i: i + m * k]:
                return True
        return False

