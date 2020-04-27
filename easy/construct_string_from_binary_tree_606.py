# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
此题目的难度还是在于理解题目的描述，
题目表述的含义就是要先序遍历二叉树，然后将每层用（）括起来，
然后再当出现空值的时候就是""，空字符串即可，使用（）括起来；
"""


class ConstructStringFromBinaryTree(object):

    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ""
        result = ""
        left = self.tree2str(t.left)
        right = self.tree2str(t.right)
        if left or right:
            result += "(" + left + ")"
        if right:
            result += "(" + right + ")"
        return str(t.val) + result
