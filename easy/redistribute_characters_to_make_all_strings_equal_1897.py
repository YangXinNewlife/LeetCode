# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是给定一个字符串数组，需要挪动任意元素的字符，
是否可以使几个元素是否一样。
可以先基于哈希算法统计每个元素个数。
这个个数必须是给定字符串元素的倍数，否则实现不了。
类似['a', 'b']这种就不行，因此必须是元素个数的倍数
"""


class RedistributeCharactersToMakeAllStringsEqual(object):

    def makeEqual(self, words: List[str]) -> bool:
        temp_dict = dict()
        for i in words:
            for j in i:
                if j not in temp_dict:
                    temp_dict[j] = 1
                else:
                    temp_dict[j] += 1
        for k in temp_dict.values():
            if k % len(words) != 0:
                return False
        return True
