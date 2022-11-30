# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是给定一个员工薪资数组，要求计算员工的平均薪资。
逻辑是去掉一个最高分、去掉一个最低分后求平均。
最后重点是要保留5位小数。
"""


class AverageSalaryExcludingTheMinimumAndMaximumSalary(object):

    def average(self, salary: List[int]) -> float:
        min_elem = min(salary)
        max_elem = max(salary)
        temp_result = list()
        for i in salary:
            if i != min_elem and i != max_elem:
                temp_result.append(i)
        result = sum(temp_result) / len(temp_result)
        return float('%.5f' % result)



