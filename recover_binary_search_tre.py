# python3
# Two elements of a binary search tree (BST) are swapped by mistake.

# Recover the tree without changing its structure.

# Note:
# A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?


# My solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res1 = None
        self.res2 = None
        self.pre = TreeNode(-float('inf'))

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        def search(node):
            if node is None:
                return
            search(node.left)
            if self.res1 == None and self.pre.val >= node.val:
                self.res1 = self.pre
            if self.res1 != None and self.pre.val >= node.val:
                self.res2 = node
            self.pre = node
            search(node.right)
            return

        search(root)
        self.res1.val, self.res2.val = self.res2.val, self.res1.val



