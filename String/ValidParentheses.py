# -*- coding:utf-8 -*-
__author__ = 'yx'
'''
括号匹配问题
'''
class Solution(object):
    def isValid(self, s):
        pars = ['']
        parmap = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in parmap and parmap[c] == pars[len(pars)-1]:
                pars.pop()
            else:
                pars.append(c)
        return len(pars) == 1
