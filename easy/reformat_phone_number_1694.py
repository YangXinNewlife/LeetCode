# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是给定一个包含数字、空格、-的字符串，需要将它按照要求
重新格式化，如下是梳理出来的规则。
规则一：长度等于5
XXX-XX
规则二：长度等于4
XX-XX
规则二：长度大于等于6
XXX-XXX...
XXX-...-XXX-XX
"""


class ReformatPhoneNumber(object):

    def reformatNumber(self, number: str) -> str:
        result = ""
        number = number.replace(" ", "").replace("-", "")
        sorted(number)
        while len(number):
            if len(number) <= 4:
                if len(number) <= 3:
                    result += number[:3]
                    number = ""
                else:
                    result += number[:2] + "-" + number[2:]
                    number = ""
            else:
                result += number[:3] + "-"
                number = number[3:]
        return result

