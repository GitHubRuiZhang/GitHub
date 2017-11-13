# python3
# The thief has found himself a new place for his thievery again. There is only one entrance to this area,
# called the "root." Besides the root, each house has one and only one parent house.
# After a tour, the smart thief realized that "all houses in this place forms a binary tree".
# It will automatically contact the police if two directly-linked houses were broken into on the same night.

# Determine the maximum amount of money the thief can rob tonight without alerting the police.

# Example 1:
#      3
#     / \
#    2   3
#     \   \
#      3   1
# Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
# Example 2:
#      3
#     / \
#    4   5
#   / \   \
#  1   3   1
# Maximum amount of money the thief can rob = 4 + 5 = 9.


# My solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        levels = []

        def search(root):
            if root is None:
                return 0, 0
            left, left_c = search(root.left)
            right, right_c = search(root.right)
            not_rob_root = left + right
            rob_root = max(not_rob_root, root.val + left_c + right_c)

            return rob_root, not_rob_root

        r, nr = search(root)

        return r

