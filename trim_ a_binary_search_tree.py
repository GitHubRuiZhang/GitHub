# python 3
# Given a binary search tree and the lowest and highest boundaries as L and R,
# trim the tree so that all its elements lies in [L, R] (R >= L).

# You might need to change the root of the tree,
# so the result should return the new root of the trimmed binary search tree.

# Example:
# Input:
#   1
# 0   2
# L = 1
# R = 2
# Output:
#   1
#     2

# Example:
# Input:
#   3
# 0   4
#  2
# 1
# L = 1
# R = 3
# Output:
#   3
#  2
# 1


# My solution
# It is accepted, but it is
# WRONG!!!!!!!!!!!!

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        return self.search(root, L, R)

    def search(self, current_node, L, R):
        if current_node is None:
            return None
        else:
            new_node_left = self.search(current_node.left, L, R)
            new_node_right = self.search(current_node.right, L, R)

        if current_node.val >= L and current_node.val <= R:
            current_node.left = new_node_left
            current_node.right = new_node_right
            return current_node
        else:
            if new_node_left is None:
                return new_node_right
            elif new_node_right is None:
                return new_node_left
                # else:
                #   we need to combine new_node_left and new_node_right to current_node.parent
                #   but it seems like in this problem, we do not need to consider this. (WRONG!!!!!!!)

# IMPORTANT:
# Remember the definition of binary search tree
# The tree additionally satisfies the binary search tree property,
# which states that the key in each node must be
# greater than or equal to any key stored in the left sub-tree,
# and less than or equal to any key stored in the right sub-tree.

# Better/Clear solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if root is None:
            return None

        if root.val < L:
            return self.trimBST(root.right, L, R)
        if root.val > R:
            return self.trimBST(root.left, L, R)

        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)

        return root


