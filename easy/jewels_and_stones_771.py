# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的意思就是一个字符串 J 代表不同的字符类型区分大小写，S 代表待匹配的字符，
那么我们只需要判断在 S 中，有多少个 J 的类型字符即可； 
"""


class JewelsAndStones(object):

    def numJewelsInStones(self, J: str, S: str) -> int:
        result = 0
        for i in range(len(S)):
            if S[i] in J:
                result += 1
        return result
