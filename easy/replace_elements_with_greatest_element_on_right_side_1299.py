# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的意思是给定一个数字 arr，
然后返回每个索引右侧最大的数字，
返回整合后的数组。
"""


class ReplaceElementsWithGreatestElementOnRightSide(object):

    def replaceElements(self, arr: List[int]) -> List[int]:
        result = list()
        max_elem = -1
        for i in arr[::-1]:
            result.append(max_elem)
            max_elem = max(max_elem, i)
        return result[::-1]
