# python3
# Reverse a linked list from position m to n.
# Do it in-place and in one-pass.

# For example:
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,

# return 1->4->3->2->5->NULL.

# Note:
# Given m, n satisfy the following condition:
# 1 ≤ m ≤ n ≤ length of list.


# My solution
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        res_head = ListNode(None)
        res_head.next = head
        node = res_head
        count = 1
        start = None
        end = None
        while node:
            if count == m:
                start = node  # start.next is the starting node
                end = node.next
            res = node.next
            if count > m + 1 and count <= n + 1 and start != None:
                node.next = start.next
                start.next = node
            if count == n + 2:
                end.next = node
                return res_head.next
            count += 1
            node = res
        end.next = None
        return res_head.next
