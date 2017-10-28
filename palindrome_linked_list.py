# python3
# Given a singly linked list, determine if it is a palindrome.

# Follow up:
# Could you do it in O(n) time and O(1) space?


# My solution
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        tail = mid = head
        while tail and tail.next:
            mid = mid.next
            tail = tail.next.next
        node_pre = None
        while mid:
            node_nex = mid.next
            mid.next = node_pre
            node_pre = mid
            mid = node_nex

        while node_pre:
            if node_pre.val != head.val:
                return False
            node_pre = node_pre.next
            head = head.next

        return True