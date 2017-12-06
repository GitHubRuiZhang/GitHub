# python3
# Sort a linked list in O(n log n) time using constant space complexity.


# My solution
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def mergeSort(head):
            if head == None or head.next == None:
                return head
            if head.next.next == None:
                if head.next.val < head.val:
                    newhead = head.next
                    newhead.next = head
                    head.next = None
                    head = newhead
                return head
            # merge sort
            fast = head
            slow = head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            right = mergeSort(slow.next)
            slow.next = None
            left = mergeSort(head)
            if left.val <= right.val:
                new_head = left
                left = left.next
            else:
                new_head = right
                right = right.next
            head = new_head
            while left and right:
                if left.val <= right.val:
                    new_head.next = left
                    left = left.next
                else:
                    new_head.next = right
                    right = right.next
                new_head = new_head.next

            if left:
                new_head.next = left
            if right:
                new_head.next = right
            return head

        return mergeSort(head)






