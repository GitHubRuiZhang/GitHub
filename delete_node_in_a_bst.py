# python3
# Given a root node reference of a BST and a key, delete the node with the given key in the BST.
# Return the root node reference (possibly updated) of the BST.

# Basically, the deletion can be divided into two stages:

# Search for a node to remove.
# If the node is found, delete the node.
# Note: Time complexity should be O(height of tree).

# Example:

# root = [5,3,6,2,4,null,7]
# key = 3

#     5
#    / \
#   3   6
#  / \   \
# 2   4   7

# Given key to delete is 3. So we find the node with value 3 and delete it.

# One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

#     5
#    / \
#   4   6
#  /     \
# 2       7

# Another valid answer is [5,2,6,null,4,null,7].

#     5
#    / \
#   2   6
#    \   \
#     4   7


# My solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """

        def search(root):
            if root is None:
                return None
            if root.left is None:
                return root
            left = search(root.left)
            return left

        res = [[root, None, 'n']]
        while res:
            cur_node_par = res.pop(0)
            cur = cur_node_par[0]
            cur_par = cur_node_par[1]
            if cur is None:
                continue
            if cur.val == key:
                if cur.left is None and cur.right is None:
                    if cur_node_par[2] == 'l':
                        cur_par.left = None
                    elif cur_node_par[2] == 'r':
                        cur_par.right = None
                    else:
                        root = None
                    return root
                elif cur.right is None:
                    if cur_node_par[2] == 'l':
                        cur_par.left = cur.left
                    elif cur_node_par[2] == 'r':
                        cur_par.right = cur.left
                    else:
                        root = cur.left
                    return root
                elif cur.left is None:
                    if cur_node_par[2] == 'l':
                        cur_par.left = cur.right
                    elif cur_node_par[2] == 'r':
                        cur_par.right = cur.right
                    else:
                        root = cur.right
                    return root
                else:
                    replace = search(cur.right)
                    replace.left = cur.left
                    if cur_node_par[2] == 'l':
                        cur_par.left = cur.right
                    elif cur_node_par[2] == 'r':
                        cur_par.right = cur.right
                    else:
                        root = cur.right
                    return root
            else:
                res.append([cur.left, cur, 'l'])
                res.append([cur.right, cur, 'r'])
        return root
