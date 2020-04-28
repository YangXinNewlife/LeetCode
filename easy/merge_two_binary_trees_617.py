# -*- encoding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的含义就是将两个二叉树合并到一起，并且如果有重合的节点，则相加；
我们只需要选择同一种递归遍历方式，然后去判断节点是否为空，求和即可；
"""


class MergeTwoBinaryTrees(object):

    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None and t2 is None:
            return
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1

