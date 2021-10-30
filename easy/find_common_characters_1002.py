# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
import collections
"""
Solutions:
题目的含义比较简单，就是判断给出的列表中重复的元素，其中重复多次的话要返回多个。
例1：
input:
["cool","lock","cook"]

output:
['c', 'o']


例2：
input:
["cool","locok","cook"]

output:
['c', 'o', 'o']

这样的话我们使用
map和collections.Counter(i)
分别作分组和统计
然后判断每个元素出现的最小值即可。
【注】：py2和py3的map是有些差异的，
py2的map返回列表、py3的map返回对象，需要list处理下。
"""


class FindCommonCharacters(object):

    def commonChars(self, words):
        result = list()
        array_count = list(map(lambda i: collections.Counter(i), words))
        for i in range(26):
            elem = chr(ord('a') + i)
            min_count = min([j[elem] for j in array_count])
            if min_count:
                result.extend([elem] * min_count)
        return result


if __name__ == '__main__':
    f = FindCommonCharacters()
    f.commonChars(["cool","lock","cook"])

