# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
import copy

"""
Solutions:
题意是给定一个数组，我们需要将数组的元素按照顺序排序，
并且返回他们每个元素排序后的顺序。
直接打表排序查找即可，但是需要注意有元素相同时，排序后的顺序就会出问题
因此这里使用dict来做过滤去重，自己保存一份排序顺序。
最后直接遍历数组查找每个元素按照我们排序后保存的顺序即可
"""


class RankTransformOfAnArray(object):

    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        result = list()
        arr_copy = copy.deepcopy(arr)
        arr_copy.sort()
        dict_sort = {}
        elem_cnt = 1
        for i in arr_copy:
            if not dict_sort.__contains__(i):
                dict_sort[i] = elem_cnt
                elem_cnt += 1
        for j in arr:
            result.append(dict_sort.get(j))
        return result

