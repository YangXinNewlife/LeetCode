# -*- coding:utf-8-
__autor__ = 'yangxin_ryan'
from collections import Counter
"""
Solutions:
题意：题目的意思给定两个输入参数
licensePlate: 输入的参照字符串
words：输入的字符串列表
要求只保留英文小写字母，然后返回words中包含licensePlate的最短的元素即可；
这里使用集合的方法Counter去统计每个word的字母出现频次，依次去对比即可；
"""


class ShortestCompletingWord(object):

    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        words = sorted(words, key=lambda x: len(x))
        license_count = Counter([x.lower() for x in licensePlate if x.isalpha()])
        for i in words:
            flag = 0
            count_i = Counter(i)
            for key, val in license_count.items():
                if key not in count_i.keys() or val > count_i[key]:
                    flag = 1
                    break
            if flag == 0:
                return i
