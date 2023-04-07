# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是给定一个字符串s,
将字符串s拆分称为两等分长度字符串fst_str和snd_str。
然后分别统计fst_str和snd_str中分别包含aeiou和AEIOU的个数，
最后判断下是否一致即可。
"""


class DetermineIfStringHalvesAreAlike(object):

    def halvesAreAlike(self, s: str) -> bool:
        fst_str = s[:len(s) // 2]
        snd_str = s[len(s) // 2:]
        vowel = "aeiouAEIOU"
        fst_cnt = 0
        snd_cnt = 0
        for i in range(len(fst_str)):
            if fst_str[i] in vowel:
                fst_cnt += 1
            if snd_str[i] in vowel:
                snd_cnt += 1
        return fst_cnt == snd_cnt





