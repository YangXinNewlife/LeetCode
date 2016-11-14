# -*- coding:utf-8 -*-
__author__ = 'jiuzhang'
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        area = (C - A) * (D - B) + (G - E) * (H - F)
        if (A >= G or B >= H or C <= E or D <= F):
            return area
        top = min(D, H)
        bottom = max(B, F)
        left = max(A, E)
        right = min(C, G)
        return area - (top - bottom) * (right - left)
