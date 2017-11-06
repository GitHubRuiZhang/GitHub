# python3
# Print a binary tree in an m*n 2D string array following these rules:

# The row number m should be equal to the height of the given binary tree.
# The column number n should always be an odd number.
# The root node's value (in string format) should be put in the exactly middle of the first row it can be put.
# The column and the row where the root node belongs will separate the rest space into two parts
# (left-bottom part and right-bottom part).
# You should print the left subtree in the left-bottom part and print the right subtree in the right-bottom part.
# The left-bottom part and the right-bottom part should have the same size.
# Even if one subtree is none while the other is not,
# you don't need to print anything for the none subtree but still need to leave the space
# as large as that for the other subtree.
# However, if two subtrees are none, then you don't need to leave space for both of them.

# Each unused space should contain an empty string "".
# print the subtrees following the same rules.
# Example 1:
# Input:
#     1
#     /
#    2
# Output:
# [["", "1", ""],
#  ["2", "", ""]]
# Example 2:
# Input:
#      1
#     / \
#    2   3
#     \
#      4
# Output:
# [["", "", "", "1", "", "", ""],
#  ["", "2", "", "", "", "3", ""],
#  ["", "", "4", "", "", "", ""]]
# Example 3:
# Input:
#       1
#      / \
#     2   5
#    /
#   3
#  /
# 4
# Output:

# [["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
#  ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
# ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
#  ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
# Note: The height of binary tree is in the range of [1, 10].


# My solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def extend(self, tree, height):
        if height <= len(tree):
            return tree
        out = [["" for i in range(2 ** height - 1)] for j in range(height)]
        for i in range(len(tree)):
            count = 2 ** i
            current_out = 2 ** (height - 1 - i) - 1
            current_tree = 2 ** (len(tree) - 1 - i) - 1
            while count > 0:
                print(current_out, current_tree)
                out[i][current_out] = tree[i][current_tree]
                count -= 1
                current_out += (2 ** (height - i))
                current_tree += (2 ** (len(tree) - i))
        return out

    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        if root is None:
            return [[""]]
        if root.left is None and root.right is None:
            return [[str(root.val)]]
        left = self.printTree(root.left)
        right = self.printTree(root.right)
        left = self.extend(left, len(right))
        right = self.extend(right, len(left))
        left.insert(0, ["" for _ in range(len(left[0]) + len(right[0]) + 1)])
        left[0][len(left[0]) // 2] = str(root.val)
        for i in range(1, len(left)):
            left[i].append("")
            left[i].extend(right[i - 1])
        return left

