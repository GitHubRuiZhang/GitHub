# python3
# Given a linked list and a value x,
# partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.


# My solution
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        less_head = ListNode(False)
        more_head = ListNode(False)
        less_node = less_head
        more_node = more_head
        node = head
        while node:
            print(node.val)
            if node.val < x:
                less_node.next = ListNode(node.val)
                less_node = less_node.next
            else:
                more_node.next = ListNode(node.val)
                more_node = more_node.next
            node = node.next

        if less_head.next is None:
            return more_head.next
        else:
            less_node.next = more_head.next
            return less_head.next
