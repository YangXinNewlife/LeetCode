# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是给定一个打字机，计算给定字符串打完需要多少步
其中移动和打字各算一步。
这里使用贪心算法min(cnt, 26 - cnt)判断向左还是向右计算
选择少的一面就可以
"""


class MinimumTimeToTypeWordUsingSpecialTypewriter(object):

    def minTimeToType(self, word: str) -> int:
        result = 0
        cur = 0
        for i in word:
            index = ord(i) - ord('a')
            cnt = index - cur
            if cnt < 0:
                cnt += 26
            result += min(cnt, 26 - cnt)
            cur = index
        return result + len(word)
