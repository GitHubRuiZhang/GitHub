# python3
# Given a binary tree, return the inorder traversal of its nodes' values.

# For example:
# Given binary tree [1,null,2,3],
#    1
#     \
#      2
#     /
#    3
# return [1,3,2].

# Note: Recursive solution is trivial, could you do it iteratively?


# My solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        out = []
        need_to_visit = [root]
        parents = [None]
        while need_to_visit:
            node = need_to_visit.pop()
            parent = parents.pop()
            if parent is not None:
                out.append(parent)
            if node is None:
                continue
            need_to_visit.append(node.right)
            parents.append(node.val)
            need_to_visit.append(node.left)
            parents.append(None)

        return out
