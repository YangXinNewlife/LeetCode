# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
逻辑就是遍历当前字符串，然后判断每个元素是否是数值，
是的话对比当前值是否比前一个大，返回True和False即可
"""


class CheckIfNumbersAreAscendingInASentence(object):

    def areNumbersAscending(self, s: str) -> bool:
        temp = -1
        cnt = 0
        for i in s.split():
            if i.isnumeric():
                if cnt == 0:
                    temp = int(i)
                    cnt += 1
                    continue
                if int(i) <= temp:
                    return False
                else:
                    temp = int(i)
        return True
