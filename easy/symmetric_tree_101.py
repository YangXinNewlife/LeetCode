# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 

Note:
Bonus points if you could solve it both recursively and iteratively.

Solution:
怎么判断一颗二叉树是Symmetric对称树
1.当root根节点为None的时候，为对称树。
2.当root根节点为非空，其左右孩子为None的时候，为对称树。
3.当root根节点为非空，其左或右孩子为None当时候，为非对称树。
4.当root根节点为非空，其左右孩子非空，但是左右孩子的val不相等的时候，为非对称树。
5.当root根节点为非空，其左右孩子非空，其左右孩子的val相等，那么再次调用函数去对比该左右孩子的左右孩子是否对称。
"""


class SymmetricTree(object):

    def isSymmetric(self, root: TreeNode) -> bool:
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
        if root is None:
            return True
        return self.judge(root.left, root.right)

    def judge(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False
        return self.judge(left.left, right.right) and self.judge(left.right, right.left)






