# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
本题目的难点在于读懂题目，题意是想要找出来出现了唯一一个的第K个数字，直接打表操作即可。
"""
import collections


class KthDistinctStringInAnArray(object):

    def kthDistinct(self, arr: List[str], k: int) -> str:
        arr_cnt = collections.Counter(arr)
        cnt = 0
        for i in arr:
            if arr_cnt[i] == 1:
                cnt += 1
                if cnt == k:
                    return i
        return ""

