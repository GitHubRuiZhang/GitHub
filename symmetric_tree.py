# python3
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following [1,2,2,null,3,null,3] is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3
# Note:
# Bonus points if you could solve it both recursively and iteratively.


# My solution I
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        left = []
        right = []

        def search(root, side):
            if root is None:
                if side == 'left':
                    left.append(None)
                else:
                    right.append(None)
            elif side == 'left':
                left.append(root.val)
                search(root.left, side)
                search(root.right, side)
            else:
                right.append(root.val)
                search(root.right, side)
                search(root.left, side)

        if root is None:
            return True
        search(root.left, 'left')
        search(root.right, 'right')
        if len(left) != len(right):
            return False
        for i in range(len(left)):
            if left[i] != right[i]:
                return False
        return True


# My solution II
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def search(left, right):
            if left is None and right is None:
                return True
            elif left is None:
                return False
            elif right is None:
                return False
            elif left.val != right.val:
                return False
            else:
                return (search(left.left, right.right) and search(left.right, right.left))

        if root is None:
            return True
        return search(root.left, root.right)
