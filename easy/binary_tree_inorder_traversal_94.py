#  -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目要求非递归的中序遍历，
中序遍历的意思其实就是先遍历左孩子、然后是根结点、最后是右孩子。我们按照这个逻辑，应该先循环到root的最左孩子，
然后依次出栈，然后将结果放入结果集合result，然后是根的val，然后右孩子。
"""


class BinaryTreeInorderTraversal(object):

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = list()
        inorder_stack = list()
        while root or inorder_stack:
            if root:
                inorder_stack.append(root)
                root = root.left
            else:
                root = inorder_stack.pop()
                result.append(root.val)
                root = root.right
        return result

