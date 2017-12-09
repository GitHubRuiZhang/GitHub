# python3
# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

# You must do this in-place without altering the nodes' values.

# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.


# My solution
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None:
            return
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        node_pre = slow
        node_cur = slow.next
        while node_cur.next:
            res = node_cur.next
            node_cur.next = res.next
            res.next = node_pre.next
            node_pre.next = res

        node = head
        large = node_pre.next
        while node != node_pre:
            node_pre.next = large.next
            large.next = node.next
            node.next = large
            node = large.next
            large = node_pre.next
        return












