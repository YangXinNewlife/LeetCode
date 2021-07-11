# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
import collections
"""
Solutions:
题意是给出一个S和T字符串，
S较短、T较长，我们判断S是不是T的有序子序列即可。
例如："abcde" 中 "ace"就是，aec就不是，其实可以用动态规划来解题。
但是这里由于是一长一短，降低了难度后。我们只需要遍历长的T字符串，S中有相同顺序的就标记/干掉一个，
最后遍历完T，如果S中都被干掉了，说明是有序的子串，否则不是。 
"""


class IsSubsequence(object):

    def isSubsequence(self, s: str, t: str) -> bool:
        queue_s = collections.deque(s)
        for i in t:
            if not queue_s:
                return True
            if i == queue_s[0]:
                queue_s.popleft()
        return not queue_s
