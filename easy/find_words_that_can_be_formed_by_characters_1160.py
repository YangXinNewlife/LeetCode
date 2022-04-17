# -*- coding:utf-8 -*-
__aithor__ = 'yangxin_ryan'
"""
Solutions:
题意是判断给定的words数组中是否可以包含chars给出的字符。
并且每个词只可以用一次，那么我们先可以通过拆分words中的词，做统计，判断是否包含chars每个即可。
我们使用统计功能即可判断如果包含，再返回时加上word长度。
"""


class FindWordsThatCanBeFormedByCharacters(object):

    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0
        for i in words:
            boolean = True
            for j in i:
                if i.count(j) > chars.count(j):
                    boolean = False
                    break
            if boolean:
                result += len(i)
        return result
