# python3
# Given a binary search tree with non-negative values,
# find the minimum absolute difference between values of any two nodes.

# Example:

# Input:

#   1
#    \
#     3
#    /
#   2

# Output:
# 1

# Explanation:
# The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
# Note: There are at least two nodes in this BST.


# My solution, there should be better solutions
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.all_values = []

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.search(root)
        self.all_values.sort()
        return min([abs(self.all_values[i + 1] - self.all_values[i]) for i in range(len(self.all_values) - 1)])
        # faster ones:
        # return min([abs(a - b) for a, b in zip(self.all_values, self.all_values[1:])])

    def search(self, root):
        if root is None:
            return
        self.all_values.append(root.val)
        self.search(root.left)
        self.search(root.right)
