# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Soultions:
题目的含义其实是根据给出的text，能够拼凑出来几个Balloons词。
只需要统计每个text元素的词的个数。
然后得处理下 str_count['l'] 和 str_count['o'] 的两次个数。
返回 str_count 这些中最少的即时凑齐的个数。
"""

class MaximumNumberOfBalloons(object);

    def maxNumberOfBalloons(self, text: str) -> int:
        str = 'balloon'
        str_count = dict.fromkeys(str, 0)
        for i in text:
            if i in str:
                str_count[i] += 1
        str_count['l'] = int(str_count['l'] / 2)
        str_count['o'] = int(str_count['o'] / 2)
        return min(str_count.values())