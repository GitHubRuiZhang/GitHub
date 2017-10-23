# python3
# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined
# between two nodes v and w as the lowest node in T that has both v and w as descendants
# (where we allow a node to be a descendant of itself).”

#        _______6______
#       /              \
#    ___2__          ___8__
#   /      \        /      \
#   0      _4       7       9
#         /  \
#         3   5
# For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6.
# Another example is LCA of nodes 2 and 4 is 2,
# since a node can be a descendant of itself according to the LCA definition.


# My solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return False

        if root == p or root == q:
            out = True
        else:
            out = False

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if out == True and (left == True or right == True):
            return root
        elif out == True:
            return True
        elif left == True and right == True:
            return root
        elif left == True or right == True:
            return True
        elif left != True and left != False:
            return left
        elif right != True and right != False:
            return right
        else:
            return False