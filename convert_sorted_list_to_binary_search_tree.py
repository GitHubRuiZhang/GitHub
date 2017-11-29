# python3
# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.


# My solution
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
            return None
        fast = head
        slow = head
        pre = None
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        root = TreeNode(slow.val)
        root.right = self.sortedListToBST(slow.next)
        if pre is not None:
            pre.next = None
            root.left = self.sortedListToBST(head)
        return root
