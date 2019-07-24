# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
这里的反转解法是利用递归的性质，每次把孩子当成root, 传递进函数。
利用深度优先遍历DFS，达到交换节点的目的。
"""


class InvertBinaryTree(object):

    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        temp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(temp)
        return root



