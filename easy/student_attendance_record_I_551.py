# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
读懂题目这道题即可有答案了。
只需要判断A和L的个数即可。
"""


class StudentAttendanceRecordI(object):

    def checkRecord(self, s: str) -> bool:
        if s.count("A") > 1 or s.count("LLL") > 0:
            return False
        else:
            return True

