# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
这里使用贪心算法。先将孩子与饼干排序。
然后某个孩子可以被满足，那就满足他。
如果饼干不能满足则继续下一个饼干，满足后 +1。
最后的 child 就是能满足的孩子数量。
"""


class AssignCookies(object):

    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        child = 0
        cookie = 0
        while child < len(g) and cookie < len(s):
            if g[child] <= s[cookie]:
                child += 1
            cookie += 1
        return child

