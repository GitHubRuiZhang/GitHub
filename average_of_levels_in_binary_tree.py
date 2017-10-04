# python3
# Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

# Example 1:
# Input:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Output: [3, 14.5, 11]
# Explanation:
# The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
# Note:
# The range of node's value is in the range of 32-bit signed integer.


# My solution, slow
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        sum_levels, num_levels = self.num_and_sum_per_level(root)
        return [sum_levels[i] / num_levels[i] for i in range(len(sum_levels))]

    def num_and_sum_per_level(self, root):
        sum_level = [float(root.val)]
        num_level = [1]
        sum_level_left = []
        num_level_left = []
        sum_level_right = []
        num_level_right = []
        if root.left is not None:
            sum_level_left, num_level_left = self.num_and_sum_per_level(root.left)

        if root.right is not None:
            sum_level_right, num_level_right = self.num_and_sum_per_level(root.right)

        sum_level.extend(
            [sum_level_left[i] + sum_level_right[i] for i in range(min(len(sum_level_left), len(sum_level_right)))])
        num_level.extend(
            [num_level_left[i] + num_level_right[i] for i in range(min(len(num_level_left), len(num_level_right)))])

        if len(sum_level_left) < len(sum_level_right):
            sum_level.extend(sum_level_right[len(sum_level_left):])
            num_level.extend(num_level_right[len(num_level_left):])
        elif len(sum_level_left) > len(sum_level_right):
            sum_level.extend(sum_level_left[len(sum_level_right):])
            num_level.extend(num_level_left[len(num_level_right):])

        return sum_level, num_level