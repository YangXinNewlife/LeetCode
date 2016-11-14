# -*- coidng:utf-8 -*-
__author__ = 'jiuzhang'
class Solution(object):
    def compareVersion(self, version1, version2):
        v1 = [int(v) for v in version1.split(".")]
        v2 = [int(v) for v in version2.split(".")]
        len1, len2 = len(v1), len(v2)
        lenmax = max(len1, len2)
        v1 += [0] * (lenmax - len1)
        v2 += [0] * (lenmax - len2)
        return 0 if v1 == v2 else 1 if v1 > v2  else -1
