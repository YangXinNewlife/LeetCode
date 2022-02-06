# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的意思就是找出来，给出数组升序排序后和原数组的差异数字个数。
方法就是现排序，然后再比较即可。
"""


class HeightChecker(object):

    def heightChecker(self, heights: List[int]) -> int:
        sorted_list = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if sorted_list[i] != heights[i]:
                count += 1
        return count

