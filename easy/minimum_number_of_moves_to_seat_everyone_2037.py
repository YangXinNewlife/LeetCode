# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是给每个人找到一个移动最小的位置。
这里直接将座椅和人的位置进行排序，
然后分别求差值即可
"""


class MinimumNumberOfMovesToSeatEveryone(object):

    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        result = 0
        seats.sort()
        students.sort()
        for i in range(len(seats)):
            if seats[i] > students[i]:
                result += seats[i] - students[i]
            elif seats[i] < students[i]:
                result += students[i] - seats[i]
        return result

