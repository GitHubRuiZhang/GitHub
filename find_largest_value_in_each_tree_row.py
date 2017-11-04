# python3
# You need to find the largest value in each row of a binary tree.

# Example:
# Input:

#           1
#          / \
#         3   2
#        / \   \
#       5   3   9

# Output: [1, 3, 9]


# My solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.largest = []

    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def search(root, depth):
            if root is None:
                return
            while len(self.largest) < depth + 1:
                self.largest.append(float('-inf'))
            self.largest[depth] = max(self.largest[depth], root.val)
            search(root.left, depth + 1)
            search(root.right, depth + 1)
            return

        search(root, 0)
        return self.largest



