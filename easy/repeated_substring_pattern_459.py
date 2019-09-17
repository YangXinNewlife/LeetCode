# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
处理这类问题的解决方法，
我们可以把原有字符串复制拼接到后面得到一个新的字符串，
如果新的字符串的自字符串[1:-1]（获取去掉瘦尾的部分）中能找到原字符串。
就返回True, 否则返回False。
"""


class RepeatedSubstringPattern(object):

    def repeatedSubstringPattern(self, s):
        """
        :param s:
        :return:
        """
        if not s:
            return False
        ss_str = s + s
        return ss_str[1:-1].find(s) != -1
