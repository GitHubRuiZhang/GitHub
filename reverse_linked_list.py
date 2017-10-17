# python3
# Reverse a singly linked list.

# Be careful about this problem

# My solution I
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        while head:
            mid = head
            head = head.next
            mid.next = pre
            pre = mid

        return pre


# My solution II
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.reverse(head, None)

    def reverse(self, head, pre):
        if head is None:
            return pre
        mid = head
        head = head.next
        mid.next = pre
        pre = mid
        return self.reverse(head, pre)