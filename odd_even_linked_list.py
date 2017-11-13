# python3
# Given a singly linked list, group all odd nodes together followed by the even nodes.
# Please note here we are talking about the node number and not the value in the nodes.

# You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

# Example:
# Given 1->2->3->4->5->NULL,
# return 1->3->5->2->4->NULL.

# Note:
# The relative order inside both the even and odd groups should remain as it was in the input.
# The first node is considered odd, the second node even and so on ...


# My solution, node value
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        node = head
        head_odd = None
        last_odd = None
        head_even = None
        last_even = None
        while node:
            if node.val % 2 == 1 and head_odd is None:
                head_odd = node
                last_odd = node
            elif node.val % 2 == 1:
                last_odd.next = node
                last_odd = node
            elif head_even is None:
                head_even = node
                last_even = node
            else:
                last_even.next = node
                last_even = node

            node = node.next

        if head_odd is None and head_even is None:
            return None
        elif head_odd is None:
            return head_even
        elif head_even is None:
            return head_odd
        else:
            last_even.next = None
            last_odd.next = head_even
            return head_odd


# My solution, node number
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        node = head
        head_odd = None
        last_odd = None
        head_even = None
        last_even = None
        odd = True
        while node:
            if odd and head_odd is None:
                head_odd = node
                last_odd = node
                odd = False
            elif odd == 1:
                last_odd.next = node
                last_odd = node
                odd = False
            elif head_even is None:
                head_even = node
                last_even = node
                odd = True
            else:
                last_even.next = node
                last_even = node
                odd = True

            node = node.next

        if head_odd is None and head_even is None:
            return None
        elif head_odd is None:
            return head_even
        elif head_even is None:
            return head_odd
        else:
            last_even.next = None
            last_odd.next = head_even
            return head_odd


