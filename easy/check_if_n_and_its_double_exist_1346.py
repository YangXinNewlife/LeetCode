# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的意思给出数组arr，找出数组中是否满足：
i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
i 和 j 为下标，因此直接实现即可。
这里稍微优化下，因为是双指针，i走到倒数第二个，j从第二个开始走。
for i in range(arr_len - 1):
for j in range(1, arr_len):
"""


class CheckIfNAndItsDoubleExist(object):

    def checkIfExist(self, arr: List[int]) -> bool:
        result = False
        arr_len = len(arr)
        for i in range(arr_len - 1):
            for j in range(1, arr_len):
                if i != j and (arr[i] == arr[j] * 2 or arr[j] == arr[i] * 2):
                    result = True
        return result
