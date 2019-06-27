# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
这里要求的返回数据是从二叉树的最后一层从左到右返回集合。
那么我们可以将问题转化为先广搜（宽搜），然后将遍历的结果逆转返回即可。
其中分层遍历使用递归方式即可。
推演过程为
[]
[[]]
[[3]]
[[3],[]]
[[3],[9]]
[[3],[9,20]]
[[3],[9,20],[]]
[[3],[9,20],[15]]
[[3],[9,20],[15,7]]
[[15,7],[9,20],[3]]
"""


class BinaryTreeLevelOrderTraversal(object):

    def levelOrderBottom(self, root):
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
        ans = []
        self.bfs(root, 0, ans)
        ans.reverse()
        return ans

    def bfs(self, root, level, ans):
        if root is not None:
            if len(ans) < level + 1:
                ans.append([])
            ans[level].append(root.val)
            self.bfs(root.left, level + 1, ans)
            self.bfs(root.right, level + 1, ans)
