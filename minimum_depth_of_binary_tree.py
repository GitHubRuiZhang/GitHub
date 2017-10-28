# python3
# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.


# My solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left != 0 and right != 0:
            return 1 + min(left, right)
        elif left == 0:
            return 1 + right
        elif right == 0:
            return 1 + left
        else:
            return 1
