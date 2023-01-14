# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目看着很复杂，其实就是括号匹配，看下完整的括号有几个即可。
直接使用数据结构的栈逻辑，凑齐一对出栈即可。
最后记录下整个进出栈过程中的最大值即可。
"""


class MaximumNestingDepthOfTheParentheses(object):

    def maxDepth(self, s: str) -> int:
        s_stack = list()
        result = 0
        for i in s:
            if i == '(':
                s_stack.append(i)
                result = max(result, len(s_stack))
            elif i == ')':
                s_stack.pop()
        return result
