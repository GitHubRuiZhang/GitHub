# python3
# Given a Binary Search Tree and a target number,
# return true if there exist two elements in the BST such that their sum is equal to the given target.

# Example 1:
# Input:
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7

# Target = 9

# Output: True

# Example 2:
# Input:
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# Target = 28
#
# Output: False


# My solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def __init__(self):
        self.possible_numbers = set()

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if root == None:
            return False
        if root.val in self.possible_numbers:
            return True
        self.possible_numbers.add(k-root.val)
        return self.findTarget(root.left,k) or self.findTarget(root.right,k)
