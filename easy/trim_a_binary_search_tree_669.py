# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
首先我们要返回的二叉搜索树，这个搜索树的功能是排序的作用，原因是因为每个节点的值要大于左孩子的值，并且小于右孩子的值；
然后给出的输入还有L、R，左右的边界，要让我们的root.val在[L, R]之间。
因此，我们只需要当
1.root.val < L，去掉左孩子以及当前节点，然后再去修剪右孩子；
2.root.val > R，去掉右孩子以及当前节点，然后再去修剪左孩子；
"""


class TrimABinarySearchTree(object):

    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if root:
            if root.val < L:
                return self.trimBST(root.right, L, R)
            elif root.val > R:
                return self.trimBST(root.left, L, R)
            else:
                root.left = self.trimBST(root.left, L, R)
                root.right = self.trimBST(root.right, L, R)
                return root
        return None



