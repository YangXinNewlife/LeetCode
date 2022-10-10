# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是给定一个字符串，要让我们消除掉a和b组成的字符串中 "回文子串"，这是重点，是回文子串 需要多少步。
其中元素只有a和b，因此如论怎么组合最多只需要2步即可消除"回文子串"。
我们利用两个指针，i = 0,j = len(s) - 1依次向中间遍历，如果元素都对称，则都是回文直接一次可以处理完，
否则就是两次。
"""


class RemovePalindromicSubsequences(object):

    def removePalindromeSub(self, s: str) -> int:
        if len(s) == 0:
            return 0
        else:
            i = 0
            j = len(s) - 1
            while i <= j:
                if s[i] != s[j]:
                    return 2
                i += 1
                j -= 1
            return 1

