# python3
# Given a binary tree, return the preorder traversal of its nodes' values.

# For example:
# iven binary tree [1,null,2,3],
#    1
#     \
#      2
#     /
#    3
# return [1,2,3].

# Note: Recursive solution is trivial, could you do it iteratively?


# My solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        out = []
        need_to_visit = [root]
        while need_to_visit:
            node = need_to_visit.pop()
            if node is None:
                continue
            out.append(node.val)
            need_to_visit.append(node.right)
            need_to_visit.append(node.left)

        return out
