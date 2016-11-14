# -*- coding:utf-8 -*-
__author__ = 'jiuzhang'
from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        if ransomNote == '':
            return True
        if magazine == '':
            return False
        note = Counter(ransomNote)
        mag = Counter(magazine)
        for i in note.keys():
            print i
            if None == mag.get(i) or not[i] > mag.get(i):
                return False
            else:
                return True



