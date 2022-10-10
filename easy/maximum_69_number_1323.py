# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是给定一个数num（只包含6 和 9）
我们可以为其中的一位将6换成9或者将9换成6，
返回当前替换后的最大值即可。
逻辑：
1.如果给出的数都是9，则返回直接返回。
2.如果给出的数据包含6和9，则直接遍历数据，挨个替换模拟对比，取出最大值即可。
"""


class Maximum69Number(object):

    def maximum69Number(self, num: int) -> int:
        result = num
        num_str = str(num)
        num_list = [int(i) for i in num_str]
        if num_list.count(9) == len(num_str):
            return result

        for j in range(len(num_str)):
            if num_str[j] == '9':
                result = max(int(num_str[:j] + '6' + num_str[j + 1:]), result)
            else:
                result = max(int(num_str[:j] + '9' + num_str[j + 1:]), result)
        return result
