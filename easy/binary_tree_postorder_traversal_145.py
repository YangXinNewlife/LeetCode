# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
递归的后序遍历法
"""


class BinaryTreePostorderTraversal(object):

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = list()
        self.post(root, result)
        return result

    def post(self, root, result):
        if root is None:
            return None
        self.post(root.left, result)
        self.post(root.right, result)
        result.append(root.val)
