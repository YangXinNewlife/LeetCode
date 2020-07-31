# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的含义就是给定S，和其中的元素C，然后给出每个S中的元素距离C的最近距离；
一般遇到这种问题我们可以使用两侧依次遍历来解决。
例子：
S = "loveleetcode", C = 'e'
从左向右遍历,判断每个元素是否为C，是的话记录为0，不是的话利用下标记录距离，这里我们使用 （下标 - 无穷小 = 无穷大）的方式来标记第一次遇到C之前的元素；
第一遍从左向右结果为如下
[inf, inf, inf, 0, 1, 0, 0, 1, 2, 3, 4, 0]
第二遍从右向左结果为如下, 第二次遍历时，
更新第一遍的结果，这里使用 min(result[i], pre - i) 来更新结果
[3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
即最后的结果
"""


class ShortestDistanceToACharacter(object):

    def shortestToChar(self, S: str, C: str) -> List[int]:
        result = []
        pre = float('-inf')
        for i, val in enumerate(S):
            if val == C:
                pre = i
            result.append(i - pre)
        pre = float('inf')
        for i in range(len(S) - 1, -1, -1):
            if S[i] == C:
                pre = i
            result[i] = min(result[i], pre - i)
        return result

