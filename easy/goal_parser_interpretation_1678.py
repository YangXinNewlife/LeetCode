# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
该题目其实可以用栈来处理，直接压栈，然后判断符合条件再出栈。
这里因为所给的元素只能拼凑G、o、al，因此直接通过下标判断即可。
"""


class GoalParserInterpretation(object):

    def interpret(self, command: str) -> str:
        result = ""
        i = 0
        while i < len(command):
            if command[i] == 'G':
                result += 'G'
                i += 1
            elif command[i] == '(' and command[i + 1] == ')':
                result += 'o'
                i += 2
            else:
                result += 'al'
                i += 4
        return result









