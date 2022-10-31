# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的意思是给出一个数num，要计算每个数所有元素的求和后分组，
例如：13
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
然后按照每个分后组的结果size排序，并返回最大的即可。
"""
import collections


class CountLargestGroup(object):

    def countLargestGroup(self, n: int) -> int:
        result_dict = {}
        for i in range(1, n + 1):
            temp_sum = self.digital_sum(i)
            if not result_dict.__contains__(temp_sum):
                result_dict[temp_sum] = 0
            result_dict[temp_sum] += 1
        return sorted(collections.Counter(result_dict.values()).items(), key=lambda x:x[0], reverse=True)[0][1]

    def digital_sum(self, num):
        result = 0
        while num > 0:
            result += num % 10
            num //= 10
        return result

