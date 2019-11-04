# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
由于题目给定的是BST，则可以知道每个节点的左子树 < root < 右子树；
那么我们可以遍历BST获取最小的差值；
"""


class MinimumAbsoluteDifferenceInBST(object):

    def getMinimumDifference(self, root: TreeNode) -> int:
        left = root.left
        right = root.right
        min_value = 0x7ffffff
        if left:
            while left.right:
                left = left.right
            min_value = min(root.val - left.val, self.getMinimumDifference(root.left))
        if right:
            while right.left:
                right = right.left
            min_value = min(min_value, right.val - root.val, self.getMinimumDifference(root.right))
        return min_value


