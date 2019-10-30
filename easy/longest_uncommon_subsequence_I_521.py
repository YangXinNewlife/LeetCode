# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的含义大家可以理解
找到最大的不同子串。
子串的定义：子序列是从一个序列导出且可以通过删除一些字符而不改变剩余元素的顺序的序列。 
简而言之，任何字符串本身都是一个子序列，空字符串是任何字符串的子序列。

因此可以分析条件有三种：
第一种，a和b字符串相等。那么没有最大子字符串，返回-1.
第二种，a和b长度相等。举个例子，aaa和aab，那么无论是aaa还是aab都是最大子字符串，所以返回len（a）或是len（b）。
第三种，a和b长度不同。举个例子，aaa和bb，那么最大子字符串一定是更长的那个字符串，即aaa。返回max（len(a),len(b)）。
"""


class LongestUncommonSubsequenceI(object):

    def findLUSlength(self, a: str, b: str) -> int:
        return -1 if a == b else max(len(a), len(b))

