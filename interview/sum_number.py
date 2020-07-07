# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Question:
给定一组无序数组，和一个目标值，我们要找出数组中两个数中和刚好等于目标值的最小的下标；
要求时间复杂度是 O(n)；

Solutions:
步骤一：这里我使用的是Hash的方式, 首先我们把给出的数组按照Hash的方式存入Hash列表（表）。
       key是元素，Value数组元素下标；
步骤二：我们去遍历给定的输入数组 list_num，并判断，（target - 数组元素） 的结果是否在的Hash表中；
如果存在的话说明hash的value不是-1，找到后break出循环，我们可以返回最小的下标；

步骤一和步骤二的时间复杂度分别是O(n)；
"""


class SumNumber(object):

    def sum_number(self, list_num, target):
        result = list()
        hash_list = [-1] * (max(max(list_num), target) + 1)
        for i in range(len(list_num)):
            if hash_list[list_num[i]] == -1:
                hash_list[list_num[i]] = i
            elif hash_list[list_num[i]] > i:
                hash_list[list_num[i]] = i
        flag = 0
        for i in range(len(list_num)):
            if hash_list[target - list_num[i]] != -1:
                result.append(i)
                result.append(hash_list[target - list_num[i]])
                flag = 1
                break
        if flag == 1:
            return result[0], result[1]
        else:
            return -1, -1


if __name__ == '__main__':
    sum_number_obj = SumNumber()
    print(sum_number_obj.sum_number([5, 4, 6, 7, 8, 11], 19))
    print(sum_number_obj.sum_number([5, 4, 6, 7, 8, 11], 11))
    print(sum_number_obj.sum_number([5, 4, 6, 7, 8, 11], 21))



