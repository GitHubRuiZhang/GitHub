# python3
# Given a binary tree, flatten it to a linked list in-place.

# For example,
# Given

#          1
#         / \
#        2   5
#       / \   \
#      3   4   6
# The flattened tree should look like:
#    1
#     \
#      2
#       \
#        3
#         \
#          4
#           \
#            5
#             \
#              6


# My solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        def search(node):
            if node is None:
                return None
            left_leaf = search(node.left)
            right_leaf = search(node.right)
            if node.left is not None and node.right is not None:
                cur = node.right
                node.right = node.left
                node.left = None
                left_leaf.right = cur
                return right_leaf
            elif node.left is not None:
                node.right = node.left
                node.left = None
                return left_leaf
            elif node.right is not None:
                return right_leaf
            else:
                return node

        search(root)
        return


