# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions：
这里使用递归的方法来处理计算左子树的和。
1.如果root为None, 则返回0
2.如果root非None,并且左孩子存储左孩子的左孩子和左孩子的右孩子不存在（说明这个左孩子是叶子节点）。
因此可以将这个左孩子的值求和。
3.然后使用递归的方式，依次遍历，找到每一个左孩子的叶子结点。
"""


class SumOfLeftLeaves(object):

    def sumOfLeftLeaves(self, root):
        """
        Definition for a binary tree node.
        class TreeNode(object):
            def __init__(self, x):
                self.val = x
                self.left = None
                self.right = None
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left and root.left.left is None and root.left.right is None:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
