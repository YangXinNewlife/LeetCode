# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
提议就是数组如果出现0元素，则复制0，并且删除最后的一个元素。
我们直接判断是否元素为0，则删除最后一个元素。直接打表通过。
"""


class DuplicateZeros(object):

    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        arr_len = len(arr)
        i = 0
        while i < arr_len:
            if arr[i] == 0:
                arr.insert(i + 1, 0)
                arr.pop()
                i += 2
            else:
                i += 1
