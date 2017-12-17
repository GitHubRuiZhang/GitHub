# python3
# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

# k is a positive integer and is less than or equal to the length of the linked list.
# If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

# You may not alter the values in the nodes, only nodes itself may be changed.

# Only constant memory is allowed.

# For example,
# Given this linked list: 1->2->3->4->5

# For k = 2, you should return: 2->1->4->3->5

# For k = 3, you should return: 3->2->1->4->5


# My solution
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or k == 1:
            return head
        count = k
        pre = head
        node = head.next
        while node and count > 1:
            node = node.next
            count -= 1
        if count > 1:
            return head
        node = head.next
        count = k
        while node and count > 1:
            res = node.next
            node.next = head
            head = node
            node = res
            count -= 1
        pre.next = self.reverseKGroup(node, k)
        return head




