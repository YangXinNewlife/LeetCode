# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目给出两个数组nums、index
其中要按照nums和index的顺序遍历nums[index]
遍历完即可，其实可以使用zip函数打包称为元组（num[i], i）即可
最后按照result.insert(i, nums[i])插入即可
"""


class CreateTargetArrayInTheGivenOrder(object):

    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = list()
        for i, j in zip(nums, index):
            result.insert(j, i)
        return result
