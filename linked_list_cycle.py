# python3
# Given a linked list, determine if it has a cycle in it.

# Follow up:
# Can you solve it without using extra space?


# My solution
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        visited = set()
        visited.add(head)
        next_node = head.next
        while next_node is not None:
            if next_node in visited:
                return True
            else:
                visited.add(next_node)
                next_node = next_node.next

        return False


# My solution II
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        if head.next is None or head.next.next is None:
            return False
        slow = head.next
        faster = head.next.next
        while faster is not None:
            if faster == slow:
                return True
            elif faster.next is None:
                return False
            else:
                faster = faster.next.next
                slow = slow.next

        return False