# -*- coding:utf-8 -*-
__author__ = 'yangxin_Ryan'
"""
Solutions:
我们可以利用递归的方式来深度遍历二叉树的叶子节点
* 当root为None，直接返回
* 当root不为空，并且没有左孩子以及右孩子，可以直接将结果存入res, 内容为 字符串间隔拼接，root ->
* 当root的左孩子为非空，我们以root.left为root，继续递归 self.dfs(root.left, path, res)
* 当root的右孩子为非空，我们以root.right为root，继续递归 self.dfs(root.right, path, res)
* 最后的 path.pop() 是由于我们开始将每个节点的val，保留下来了。path.append(str(root.val))，
方便拼接。
"""


class BinaryTreePaths(object):

    def binaryTreePaths(self, root):
        """
          Definition for a binary tree node.
          class TreeNode(object):
              def __init__(self, x):
                  self.val = x
                  self.left = None
                  self.right = None

        :type root: TreeNode
        :rtype: List[str]
        """
        res, path = [], []
        self.dfs(root, path, res)
        return res

    def dfs(self, root, path, res):
        if not root:
            return
        path.append(str(root.val))
        if not root.left and not root.right:
            res.append('->'.join(path))
        if root.left:
            self.dfs(root.left, path, res)
        if root.right:
            self.dfs(root.right, path, res)
        path.pop()




