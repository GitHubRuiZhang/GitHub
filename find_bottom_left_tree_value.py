# python3
# Given a binary tree, find the leftmost value in the last row of the tree.

# Example 1:
# Input:

#     2
#    / \
#   1   3

# Output:
# 1
# Example 2:
# Input:

#         1
#        / \
#       2   3
#      /   / \
#     4   5   6
#        /
#       7

# Output:
# 7
# Note: You may assume the tree (i.e., the given root node) is not NULL.


# My solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def search(root, depth):
            if root is None:
                return None
            left = search(root.left, depth + 1)
            right = search(root.right, depth + 1)
            if left is not None and right is not None:
                if left[0] >= right[0]:
                    return left
                else:
                    return right
            elif left is not None:
                return left
            elif right is not None:
                return right
            else:
                return [depth + 1, root.val]

        out = search(root, 0)
        return out[1]


