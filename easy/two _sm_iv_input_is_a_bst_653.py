# -*- coidng:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目让我们去判断是否给定的数字K是由搜索二叉树中的两个数字的和；
因此我们可以利用减法，我们遍历二叉树的每个节点，并加入data_set集合中，然后
遍历的时候用k和每个元素做剪发，看一下是否结果包含在存储的data_set集合中即可；
"""


class TwoSumIVInputISABST(object):

    def findTarget(self, root: TreeNode, k: int) -> bool:

        data_set = set()

        def dfs(root):
            if not root:
                return False
            if k - root.val in data_set:
                return True
            data_set.add(root.val)
            return dfs(root.left) or dfs(root.right)
        return dfs(root)


