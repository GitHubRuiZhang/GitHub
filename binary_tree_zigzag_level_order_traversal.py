# python3
# Given a binary tree, return the zigzag level order traversal of its nodes' values.
# (ie, from left to right, then right to left for the next level and alternate between).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]


# My solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        out = []

        def search(root, level):
            if root is None:
                return
            if len(out) == level:
                out.append([root.val])
            else:
                out[level].append(root.val)
            search(root.left, level + 1)
            search(root.right, level + 1)
            return

        search(root, 0)
        for i in range(len(out)):
            if i % 2 == 1:
                out[i] = out[i][::-1]
        return out


