# python3
# Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

# Calling next() will return the next smallest number in the BST.

# Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.


# My solution
# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        nodes = [self.root]
        self.val = []
        while nodes:
            cur = nodes.pop(0)
            if cur is None:
                continue
            self.val.append(cur.val)
            nodes.append(cur.left)
            nodes.append(cur.right)

        self.val.sort()

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.val) != 0

    def next(self):
        """
        :rtype: int
        """
        return self.val.pop(0)



        # Your BSTIterator will be called like this:
        # i, v = BSTIterator(root), []
        # while i.hasNext(): v.append(i.next())