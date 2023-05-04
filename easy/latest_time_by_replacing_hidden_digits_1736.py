# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意其实就是处理给定时间且隐藏起来的数字，
HH:MM格式
HH，最大24
MM，最大59
基于这个规则拆分逻辑实现即可
"""


class LatestTimeByReplacingHiddenDigits(object):

    def maximumTime(self, time: str) -> str:
        time_list = list(time)
        if time_list[0] == '?':
            if time_list[1] == '?':
                time_list[0], time_list[1] = '2', '3'
            elif time_list[1] <= '3':
                time_list[0] = '2'
            else:
                time_list[0] = '1'
        elif time_list[1] == '?':
            if time_list[0] == '2':
                time_list[1] = '3'
            else:
                time_list[1] = '9'
        if time_list[3] == '?':
            time_list[3] = '5'
        if time_list[4] == '?':
            time_list[4] = '9'
        return ''.join(time_list)

