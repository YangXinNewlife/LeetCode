# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solution
题意就是基于给定字符串
然后基于空格分隔后去最后一位最为排序的下标
最后返回排序后的字符串
使用哈希算法即可
"""


class SortingTheSentence(object):

    def sortSentence(self, s: str) -> str:
        s = s.split(" ")
        result = [None] * len(s)
        for i in s:
            result[int(i[-1]) - 1] = i[:-1]
        return ' '.join(result)

demo = SortingTheSentence()
demo.sortSentence("is2 sentence4 This1 a3")




