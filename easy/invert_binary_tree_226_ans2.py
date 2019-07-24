# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
这里的反转解法是非递归的方式，我们利用栈数据结构，将每一个孩子节点放进去
先进后出的方式达到反转的目的。
"""


class InvertBinaryTree(object):

    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        stack = [root]
        while len(stack) != 0:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.roght:
                stack.append(node.right)
        return root


