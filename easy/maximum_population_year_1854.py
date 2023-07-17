# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目就是计算下人口最多的那年
其实就是遍历数组，然后计算下每年的人数，
返回最大的值即可
"""


class MaximumPopulationYear(object):

    def maximumPopulation(self, logs: List[List[int]]) -> int:
        person_dict = dict()
        for i, j in logs:
            person_dict[i] = person_dict.get(i, 0) + 1
            person_dict[j] = person_dict.get(j, 0) - 1
        temp = 0
        temp_max = 0
        for k in range(1950, 2051):
            temp += person_dict.get(k, 0)
            if temp > temp_max:
                temp_max = temp
                result = k
        return result
