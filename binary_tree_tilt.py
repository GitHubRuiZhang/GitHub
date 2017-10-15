# python3
# Given a binary tree, return the tilt of the whole tree.

# The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and
# the sum of all right subtree node values. Null node has tilt 0.

# The tilt of the whole tree is defined as the sum of all nodes' tilt.

# Example:
# Input:
#          1
#        /   \
#       2     3
# Output: 1
# Explanation:
# Tilt of node 2 : 0
# Tilt of node 3 : 0
# Tilt of node 1 : |2-3| = 1
# Tilt of binary tree : 0 + 0 + 1 = 1
# Note:

# The sum of node values in any subtree won't exceed the range of 32-bit integer.
# All the tilt values won't exceed the range of 32-bit integer.


# My solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        root_tilt = self.findTiltandSum(root)
        return root_tilt[1]

    def findTiltandSum(self, root):
        if root is None:
            return [0, 0]
        result_left = self.findTiltandSum(root.left)
        result_right = self.findTiltandSum(root.right)
        root_tilt = result_left[1] + result_right[1] + abs(result_left[0] - result_right[0])
        root_sum = root.val + (result_left[0] + result_right[0])
        return [root_sum, root_tilt]
