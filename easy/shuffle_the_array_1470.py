# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是给定一个数组，一个切分的长度n，
然后将两个数组打平即可。
这里可以通过zip函数打平后在遍历即可。
"""


class ShuffleTheArray(object):

    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = list()
        for i, j in zip(nums[:n], nums[n:]):
            result.append(i)
            result.append(j)
        return result
