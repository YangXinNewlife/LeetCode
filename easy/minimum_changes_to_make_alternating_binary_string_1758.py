# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是给定只有包含0和1的字符串，
需要判断下是否是相邻两个元素是不同的。
如果不是的话，需要将字符串弄成相邻的字符串即可。
思路：
基于给定字符串s，构建出两个由0和1分别开头的模版字符串
temp_str1，temp_str2
然后分别去对比字符串 s 的每个元素，
返回相差最小的元素个数。
"""


class MinimumChangesToMakeAlternatingBinaryString(object):

    def minOperations(self, s: str) -> int:
        result1, result2 = 0, 0
        len_str = len(s)
        if len_str % 2 == 1:
            temp_str1 = "10" * (len_str // 2) + "1"
            temp_str2 = "01" * (len_str // 2) + "0"
        else:
            temp_str1 = "10" * (len_str // 2)
            temp_str2 = "01" * (len_str // 2)
        for i in range(len_str):
            if temp_str1[i] != s[i]:
                result1 += 1
            if temp_str2[i] != s[i]:
                result2 += 1
        return min(result1, result2)


