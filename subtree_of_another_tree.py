# python3
# Given two non-empty binary trees s and t,
# check whether tree t has exactly the same structure and node values with a subtree of s.
# A subtree of s is a tree consists of a node in s and all of this node's descendants.
# The tree s could also be considered as a subtree of itself.

# Example 1:
# Given tree s:
#
#      3
#     / \
#    4   5
#   / \
#  1   2
# Given tree t:
#    4
#   / \
#  1   2
# Return true, because t has the same structure and node values with a subtree of s.

# Example 2:
# Given tree s:
#
#      3
#     / \
#    4   5
#   / \
#  1   2
#     /
#    0
# Given tree t:
#    4
#   / \
#  1   2
# Return false.


# My solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        def check(root1, root2):
            if root1 == None and root2 == None:
                return True
            elif root1 != None and root2 == None:
                return False
            elif root1 == None and root2 != None:
                return False
            elif root1.val != root2.val:
                return False
            return check(root1.left, root2.left) and check(root1.right, root2.right)

        def search(root, root_sub):
            if root is None:
                return False
            if root.val == root_sub.val:
                if check(root, root_sub):
                    return True
            return search(root.left, root_sub) or search(root.right, root_sub)

        if s == None and t == None:
            return True
        elif s != None and t != None:
            return search(s, t)
        else:
            return False


