# python3
# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.


# My solution
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None and l2 == None:
            return None
        elif l1 == None:
            return l2
        elif l2 == None:
            return l1
        else:
            new_list = None
            if l1.val > l2.val:
                new_list = l2
                new_list.next = self.mergeTwoLists(l1, l2.next)
            else:
                new_list = l1
                new_list.next = self.mergeTwoLists(l2, l1.next)
            return new_list


