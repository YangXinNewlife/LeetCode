# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是每一个单元格都是一个节点，每个节点还可以分是否是叶子节点（内部没有再嵌套），然后可以进行或运算，
T or T = T
T or F = T
F or F = F
计算公式如上，我们只需要将每个单元格的进行计算即可。
"""


class QuadTreeIntersection(object):

    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        """
        # Definition for a QuadTree node.
        class Node:
            def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
                self.val = val
                self.isLeaf = isLeaf
                self.topLeft = topLeft
                self.topRight = topRight
                self.bottomLeft = bottomLeft 
                self.bottomRight = bottomRight
        :param quadTree1:
        :param quadTree2:
        :return:
        """
        if quadTree1.isLeaf:
            return quadTree1 if quadTree1.val else quadTree2
        if quadTree2.isLeaf:
            return quadTree2 if quadTree2.val else quadTree1
        quadTree1.topLeft = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        quadTree1.topRight = self.intersect(quadTree1.topRight, quadTree2.topRight)
        quadTree1.bottomLeft = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        quadTree1.bottomRight = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)
        if quadTree1.topLeft.isLeaf and quadTree1.topRight.isLeaf and quadTree1.bottomLeft.isLeaf and quadTree1.bottomRight.isLeaf:
            if quadTree1.topLeft.val == quadTree1.topRight.val == quadTree1.bottomLeft.val == quadTree1.bottomRight.val:
                quadTree1.isLeaf = True
                quadTree1.val = quadTree1.topLeft.val
        return quadTree1


