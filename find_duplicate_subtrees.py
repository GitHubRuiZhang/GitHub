# python3
# Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees,
# you only need to return the root node of any one of them.

# Two trees are duplicate if they have the same structure with same node values.

# Example 1:
#         1
#        / \
#       2   3
#      /   / \
#     4   2   4
#        /
#       4
# The following are two duplicate subtrees:
#       2
#      /
#     4
# and
#     4
# Therefore, you need to return above trees' root in the form of a list.


# My solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        all_roots = {}

        def search(root):
            if root is None:
                return None
            cur = (root.val, search(root.left), search(root.right))
            if cur in all_roots:
                all_roots[cur].append(root)
            else:
                all_roots[cur] = [root]

            return cur

        search(root)
        out = []
        for key in all_roots.keys():
            if len(all_roots[key]) > 1:
                out.append(all_roots[key][0])

        return out


