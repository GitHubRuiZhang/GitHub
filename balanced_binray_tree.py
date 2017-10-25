# python3
# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees
# of every node never differ by more than 1.


# My solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def search(root):
            if root is None:
                return True, 0
            left, left_height = search(root.left)
            right, right_height = search(root.right)
            if left is False or right is False:
                return False, (max(left_height, right_height) + 1)
            if abs(left_height - right_height) > 1:
                return False, (max(left_height, right_height) + 1)

            return True, (max(left_height, right_height) + 1)

        if root is None:
            return True
        result, height = search(root)
        return result

