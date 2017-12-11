# python3
# Given a list, rotate the list to the right by k places, where k is non-negative.


# Example:

# Given 1->2->3->4->5->NULL and k = 2,

# return 4->5->1->2->3->NULL.


# My solution
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # naive
        if not head:
            return None
        node = head
        all_nodes = []
        while node:
            all_nodes.append(node)
            node = node.next

        if k > len(all_nodes):
            k %= len(all_nodes)
        if k == len(all_nodes) or k == 0:
            return head
        new_head = all_nodes[-k]
        all_nodes[-1].next = all_nodes[0]
        all_nodes[-k - 1].next = None

        return new_head



