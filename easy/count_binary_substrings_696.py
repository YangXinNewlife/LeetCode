# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是计算给定的字符串中有多少个连续、相邻的子串；
例如：00110011
子串：0011、01、10、1100、01、0011
这里为什么00110011不是，原因是001100的00和00中间隔着11，不连续所以不是，那么我们可以设定两个指针pre（旧的） ,cur（当前的）
pre与cur依次交替记录上一个00...或者11...
过程模拟：
index代表下标， value代表下标对应的值
-- 00110011
index = 0, value = 0
cur = 1
pre = 0
index = 1, value = 0
cur = 2
pre = 0
index = 2, value = 1
cur = 1
pre = 2
index = 3, value = 1
cur = 2
pre = 2
因为index = 4的时候value = 0
所以我们这里要做一个比较最小值，为什么比较最小值呢？因为00111时，只能构成0011、01，两种，原因是选择00或者111里面长度小的，
所以我们只需要每次比较cur和pre中较小的，然后保存较小的，进入下一个pre和cur中；
"""


class CountBinarySubstrings(object):

    def countBinarySubstrings(self, s: str) -> int:
        result = 0
        len_s = len(s)
        cur_count = 0
        i = 0
        while i < len_s:
            pre_count = cur_count
            cur_count = 1
            i += 1
            while i < len_s and s[i] == s[i-1]:
                cur_count += 1
                i += 1
            result += min(pre_count, cur_count)
        return result

