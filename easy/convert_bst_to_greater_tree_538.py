# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Soultions:
题目大意是给定一个BST 二叉搜索树（内部有序，左孩子小于root，小于右孩子）。然后把每一个大于当前节点的值加到当前节点。
那么一个好的思路就是从最大加到最小。（假如从最小开始计算，那么每次都要更新一次所有比他大的，会有大量重复的计算）。
"""


class ConvertBSTToGreaterTree(object):

    def convertBST(self, root) -> TreeNode:
        """
        Definition for a binary tree node.
        class TreeNode:
            def __init__(self, x):
                self.val = x
                self.left = None
                self.right = None
        :param root:
        :return:
        """
        self.temp_sum = 0
        self.after_order(root)
        return root

    def after_order(self, child):
        if not child:
            return
        self.after_order(child.right)
        self.temp_sum += child.val
        child.val = self.temp_sum
        self.after_order(child.left)
