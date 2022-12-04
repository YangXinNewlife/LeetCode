# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目比较简单，直接按照公式要求三重循环即可，打表通过。
"""


class CountGoodTriplets(object):

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        length = len(arr)
        result = 0
        for i in range(length - 2):
            for j in range(i + 1, length - 1):
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j + 1, length):
                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            result += 1
        return result


