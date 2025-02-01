# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solution:
题意说道是给定一组字符串，和一个前缀字符串pref，我们判断给定数组中的字符串如果包含这个前缀的，记一个。
最后看下有多少个字符串符合这个规则即可
"""
class CountingWordsWithAGivenPrefix(object):

    def prefixCount(self, words: List[str], pref: str) -> int:
        result = 0
        for i in words:
            if str(i).startswith(pref):
                result += 1
        return result