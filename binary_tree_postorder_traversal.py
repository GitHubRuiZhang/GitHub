# python3
# Given a binary tree, return the postorder traversal of its nodes' values.

# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [3,2,1].

# Note: Recursive solution is trivial, could you do it iteratively?


# My solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        out = []
        need_to_visit = []
        p = root
        while need_to_visit or p != None:
            if p is not None:
                need_to_visit.append(p)
                out.append(p.val)
                p = p.right
            else:
                node = need_to_visit.pop()
                p = node.left

        return out[::-1]
