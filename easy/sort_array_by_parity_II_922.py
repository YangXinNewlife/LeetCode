# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的含义就是把给定的数组按照奇数位是奇数，偶数位是偶数即可。
"""


class SortArrayByParityII(object):

    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        result = list()
        odd_list = [i for i in nums if i % 2 == 1]
        even_list = [j for j in nums if j % 2 == 0]
        is_even = True
        while odd_list or even_list:
            if is_even:
                result.append(even_list.pop())
            else:
                result.append(odd_list.pop())
            is_even = not is_even
        return result


