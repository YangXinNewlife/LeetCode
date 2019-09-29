# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
思路是先处理原字符串带有的-，然后转换成为无-的字符串，
然后根据L的个数来做分配
"""


class LicenseKeyFormatting(object):

    def licenseKeyFormatting(self, S, K):
        """
        :param S: 原字符串
        :param K: K的大小，-分割每个字符串的大小
        :return:
        """
        s_up = S.upper()
        str_s = ''.join(s_up.split('-'))
        if K == 1:
            return '-'.join(str_s)
        result = ''
        count = 0
        i = len(str_s)
        while i > K:
            result = str_s[i - K: i] + result
            result = '-' + result
            i -= K
            count += K
        result = str_s[0:len(str_s) - count] + result
        return result

