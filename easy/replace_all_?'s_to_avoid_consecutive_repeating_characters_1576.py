# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'

"""
Solutions:
题目就是将字符串中的？替换为小写的字符。
要求是相邻的不能一样。那么格式就得要求连着两个不相邻，
xxx -> abc 就可以用三个字符代替。
"""


class ReplaceAllSToAvoidConsecutiveRepeatingCharacters(object):

    def modifyString(self, s: str) -> str:
        result = list()
        replace_char = ''
        s_len = len(s)
        for i, char in enumerate(s):
            if char == '?':
                if replace_char != 'a' and (i + 1 >= s_len or s[i + 1] != 'a'):
                    result.append('a')
                    replace_char = 'a'
                elif replace_char != 'b' and (i + 1 >= s_len or s[i + 1] != 'b'):
                    result.append('b')
                    replace_char = 'b'
                else:
                    result.append('c')
                    replace_char = 'c'
            else:
                result.append(s[i])
                replace_char = s[i]
        return ''.join(result)


