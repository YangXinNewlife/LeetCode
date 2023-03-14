# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是判断给定的words中有多少个字段串均是由allowed中的构成
"""


class CountTheNumberOfConsistentStrings(object):

    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        result = 0
        allowed = set(allowed)
        for i in words:
            for j in i:
                if j not in allowed:
                    result += 1
                    break
        return len(words) - result

