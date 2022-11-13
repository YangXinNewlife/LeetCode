# -*- coding:utf-8 -*-
___author__ = 'yangxin_ryan'
"""
Solutions:
题目的意思是判断给定的queryTime是否在startTime[i]和endTime[i]区间内即可，
看懂题目应该就没啥问题
"""

class NumberOfStudentsDoingHomeworkAtAGivenTime(object):

    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) ->
        result = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                result += 1
        return result


