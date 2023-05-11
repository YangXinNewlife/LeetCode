# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意就是给定一个高和低的范围，
然后分别计算高和低数据范围每个数字的各个元素求和，
然后分别利用哈希的方式，放入对应求和结果下标的字典中。
最后求最大值即可。
"""
import collections


class MaximumNumberOfBallsInABox(object):

    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        result_dict = collections.defaultdict(int)
        for i in range(lowLimit, highLimit + 1):
            result_dict[self.cnt(str(i))] += 1
        return max(result_dict.values())

    def cnt(self, number):
        temp_cnt = 0
        for j in number:
            temp_cnt += int(j)
        return temp_cnt
