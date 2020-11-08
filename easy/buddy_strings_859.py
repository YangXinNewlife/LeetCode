# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的意思是为了找出两个小写字符串A、B。并且随意选择交换A的位置可以等于另外一个B的；
那么我们可以先分析，例如是否可以排除长度不相等的，并且差异字符存在1或者大于2的（为因为符合这两个的没办法交换相等）
则返回False，其余就是返回True即可；
"""


class BuddyStrings(object):

    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        diff_cnt = 0
        diff_list = []
        for i, j in enumerate(A):
            if B[i] != j:
                diff_cnt += 1
                diff_list.append(i)
        if diff_cnt not in [0, 2]:
            return False
        if diff_cnt == 0 and len(set(A)) < len(A):
            return True
        if diff_cnt == 2:
            list_1 = list(A)
            list_1[diff_list[0]], list_1[diff_list[1]] = list_1[diff_list[1]], list_1[diff_list[0]]
            if list_1 == list(B):
                return True
        return False


