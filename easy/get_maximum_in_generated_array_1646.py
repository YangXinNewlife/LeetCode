# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意其实就是给定一个数据n，然后在长度为n的大小数组中找到计算后元素最大的值，
将n的数据从2开始分奇数和偶数进行计算。
偶数：result.append(result[i // 2])
奇数：result.append(result[i // 2] + result[i // 2 + 1])
最后返回最大的即可
"""


class GetMaximumInGeneratedArray(object):

    def getMaximumGenerated(self, n: int) -> int:
        if n < 2:
            return n
        result = list()
        result.append(0)
        result.append(1)
        for i in range(2, n + 1):
            if i % 2 == 0:
                result.append(result[i // 2])
            else:
                result.append(result[i // 2] + result[i // 2 + 1])
        return max(result)

