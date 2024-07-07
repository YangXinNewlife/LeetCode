# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意就是判断出第K个人买完所有票需要多长时间，
可以先找所有人都买完的思路计算共需要 people_cnt * (tickets[k] - 1) + k + 1 
然后在去掉比自己少的部分和排在自己后面的人比自己多的部分。
"""


class TimeNeededToBuyTickets(object):

    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        people_cnt = len(tickets)
        result = people_cnt * (tickets[k] - 1) + k + 1
        for i in range(k):
            if tickets[i] < tickets[k]:
                result -= tickets[k] - tickets[i]
        for j in range(k + 1, people_cnt):
            if tickets[j] < tickets[k] - 1:
                result -= tickets[k] - 1 - tickets[j]
        return result

