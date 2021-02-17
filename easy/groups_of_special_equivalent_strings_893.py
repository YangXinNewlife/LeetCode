# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意：
给出一组字符串，我们认为将某个字符串的奇数位和偶数位交换得到一样的字符串，我们认为就是一组，求一共有多少组字符串；
思路：
我们认为可以使用set来保留一组的结果（去重），然后将奇数位和偶数位的分别抽取并且组合到一起，看看一共有几组；
"""


class GroupsOfSpecialEquivalentStrings(object):

    def numSpecialEquivGroups(self, A: List[str]) -> int:
        return len(set(''.join(sorted(a[0::2])) + ''.join(sorted(a[1::2])) for a in A))

