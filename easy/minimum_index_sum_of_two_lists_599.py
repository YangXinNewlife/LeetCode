# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
这里先使用Hash的思想将list1的数据存储到dict类型的data_dict中，然后遍历list2元素判断是否在data_dict中，
若在的话求索引之和，然后判断当前索引的大小，如果小于，则清空存储索引的list后在做存储，如果相等则追加即可；
"""


class MinimumIndexSumOfTwoLists(object):

    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_index = 2000
        data_dict = {}
        result = list()
        for i in range(len(list1)):
            data_dict[list1[i]] = i
        for j in range(len(list2)):
            if list2[j] in data_dict and data_dict[list2[j]] + j < min_index:
                min_index = data_dict[list2[j]] + j
                result.clear()
                result = [list2[j]]
            elif list2[j] in data_dict and data_dict[list2[j]] + j == min_index:
                result.append(list2[j])
        return result




