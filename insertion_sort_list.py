# python3
# Sort a linked list using insertion sort.


# My solution
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def insert(head, tail, target):
            # special case, insert target at head
            if head.val >= target.val:
                target.next = head
                return [target, tail]

            # normal case
            node = head
            while node.next and node.next.val < target.val:
                node = node.next
            res = node.next
            node.next = target
            target.next = res
            if res == None:
                return [head, target]
            else:
                return [head, tail]

        if head is None:
            return None
        node = head.next
        pre = head
        while node:
            # cut the nodes into three parts: sorted, node, unsorted
            tail = node.next  # start of the unsorted nodes
            node.next = None  # cut the node from unsorted nodes
            pre.next = None  # only iterate the sorted nodes to find the position of the node
            # insert the current node into the sorted nodes
            res = insert(head, pre, node)
            head = res[0]
            head_tail = res[1]
            # connect the sorted nodes with unsorted nodes
            head_tail.next = tail
            # iterate to next node
            node = tail
            pre = head_tail
        return head
