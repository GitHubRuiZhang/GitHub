# python3
# Given the root of a tree, you are asked to find the most frequent subtree sum.
# The subtree sum of a node is defined as the sum of all the node values
# formed by the subtree rooted at that node (including the node itself).
# So what is the most frequent subtree sum value? If there is a tie,
# return all the values with the highest frequency in any order.

# Examples 1
# Input:
#   5
#  /  \
# 2   -3
# return [2, -3, 4], since all the values happen only once, return all of them in any order.

# Examples 2
# Input:
#   5
#  /  \
# 2   -5
# return [2], since 2 happens twice, however -5 only occur once.
# Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer.


# My solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.count = {}

    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def search(root):
            if root is None:
                return 0
            left = search(root.left)
            right = search(root.right)
            current = root.val + left + right
            if current in self.count:
                self.count[current] += 1
            else:
                self.count[current] = 1

            return current

        search(root)
        out = []
        current_times = 0
        for key in self.count:
            if self.count[key] > current_times:
                current_times = self.count[key]
                out = [key]
            elif self.count[key] == current_times:
                out.append(key)

        return out
