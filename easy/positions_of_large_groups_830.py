# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的意思比较简单，就是找出来最长的相同的字符串，字符的连续长度要大于等于3。
这里的解决方法是因为所有的字符都是小写字符，我们加一个非小写的字符在最后 S = S + "A"，
用作字符串的结尾，这时我们只需要维护一个临时的list，我们判断两个相邻的元素是否一致，一致的话就添加到临时组里；
"""


class PositionsOfLargeGroups(object):

    def largeGroupPositions(self, S: str) -> List[List[int]]:
        S = S + "A"
        group = list()
        pre_index = 0
        pre_elem = ""
        for i, j in enumerate(S):
            if not pre_elem:
                pre_elem = j
                pre_index = i
            elif pre_elem != j:
                if i - pre_index >= 3:
                    group.append([pre_index, i - 1])
                pre_index = i
                pre_elem = j
        return group
