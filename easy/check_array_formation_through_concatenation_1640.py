# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的含义其实是判断可以挪动pieces的每个元素的情况下，
是否可以和之前的arr数组保持一致，
例1：arr = [91,4,64,78], pieces = [[78],[4,64],[91]] 就可以
例2：arr = [49,18,16], pieces = [[16,18,49]] 就不行，因为pieces的元素只有一个，无法挪动
这里其实只需要判断数组中每个层级是否完整即可。只要局部可以挪动，
就可以在局部形成一致，如果局部都不一致，那么整体则无法一致。
"""


class CheckArrayFormationThroughConcatenation(object):

    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        i = 0
        piece_dict = {}
        for piece in pieces:
            piece_dict[piece[0]] = piece
        print(piece_dict)
        while i < len(arr):
            now = arr[i]
            if now not in piece_dict:
                return False
            piece = piece_dict[now]
            for j in piece:
                if j != arr[i]:
                    return False
                i += 1
        return True
