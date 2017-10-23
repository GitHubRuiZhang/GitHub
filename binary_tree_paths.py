# python3
# Given a binary tree, return all root-to-leaf paths.

# For example, given the following binary tree:

#    1
#  /   \
# 2     3
#  \
#   5
# All root-to-leaf paths are:

# ["1->2->5", "1->3"]


# My solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        out = []

        def search(root, pre):
            if root == None:
                return
            if pre == None:
                out.append(str(root.val))
                pre = 0
            else:
                out[pre] = out[pre] + '->' + str(root.val)

            if root.left is not None and root.right is not None:
                out.append(out[pre])
                search(root.right, len(out) - 1)
                search(root.left, pre)
            elif root.left is not None:
                search(root.left, pre)
            elif root.right is not None:
                search(root.right, pre)

            return

        search(root, None)
        return out
