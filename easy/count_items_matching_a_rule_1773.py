# -*- coding:utf-8 -*-
__author__ = 'yangxin'
"""
Solutions:
题意：
给定每一个Item都有三个元素属性，类型、颜色和名字
然后给定一个规则ruleKey，我们基于ruleKey去判断是筛选"属性"、"颜色"还是名字属性
然后计算命中的item的数量，直接基于描述先判断再统计即可。
"""


class CountItemsMatchingARule_1773(object):

    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        result = 0
        if ruleKey == 'type':
            key = 0
        elif ruleKey == 'color':
            key = 1
        else:
            key = 2
        for i in items:
            if i[key] == ruleValue:
                result += 1
        return result

