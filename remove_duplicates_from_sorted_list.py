# python3
# Given a sorted linked list, delete all duplicates such that each element appear only once.

# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.


# My solution
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        original_head = head
        while head.next:
            next_node = head.next
            if next_node.val == head.val:
                head.next = next_node.next
            else:
                head = next_node
        return original_head

