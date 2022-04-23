# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的含义其实就是给定年、月、日三个数，然后我们判断给定这天是周几。
我们可以构造week列表，然后判断出是一周的第几天后，直接返回下标对应的值。
"""
from datetime import date


class DayOfTheWeek(object):

    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        week_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return week_list[date(year, month, day).weekday()]

