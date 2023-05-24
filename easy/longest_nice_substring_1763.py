# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意就是判断下给定的字符串s中，
有那些是既有同一个字母的大小和小写的子串
例如 s = "YazaAay"
中的Nice子串是aAa、Ya
其中最长的Nice子串是aAa 
我们分别去构建一个主双循环遍历处理逻辑
和一个检查check函数
check用于检查字符串str是否是nice子串
"""


class LongestNiceSubstring(object):

    def longestNiceSubstring(self, s: str) -> str:
        result = ""
        cnt = 0
        sub_str = list()
        for i in range(len(s)):
            for j in range(i):
                temp_str = s[j: i + 1]
                if temp_str not in sub_str:
                    sub_str.append(temp_str)
        for k in sub_str:
            if self.check(k):
                if len(k) > cnt:
                    cnt = len(k)
                    result = k
        return result

    def check(self, param):
        temp_list = list()
        for i in param:
            if i not in temp_list:
                temp_list.append(i)
        for j in temp_list:
            if str(j).islower() and str(j).capitalize() not in temp_list:
                return False
            elif str(j).isupper() and str(j).lower() not in temp_list:
                return False
        return True






















