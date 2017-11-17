# python3
# Given a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.

# For example:
# Given the following binary tree,
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---
# You should return [1, 3, 4].


# My solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        out = []
        nodes = [[root, 1]]
        while nodes:
            print(nodes, out)
            cur = nodes.pop(0)
            if cur[0] is None:
                continue
            if len(out) < cur[1]:
                out.append(cur[0].val)
            nodes.append([cur[0].right, cur[1] + 1])
            nodes.append([cur[0].left, cur[1] + 1])

        return out


