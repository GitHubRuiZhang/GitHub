# python3
# Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1...n.

# For example,
# Given n = 3, your program should return all 5 unique BST's shown below.

#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3


# My solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        def build(nums):
            if len(nums) == 0:
                return [None]
            if len(nums) == 1:
                return [TreeNode(nums[0])]
            out = []
            for i in range(len(nums)):
                cur = TreeNode(nums[i])
                left = build(nums[:i])
                right = build(nums[i + 1:])
                for itl in left:
                    for itr in right:
                        cur = TreeNode(nums[i])
                        cur.left = itl
                        cur.right = itr
                        out.append(cur)

            return out

        out = build([i + 1 for i in range(n)])
        if out == [None]:
            return []
        return out




