# python3
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.


# My solution
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        out = []
        while True:
            pre = len(out)
            for i in range(len(lists)):
                if lists[i] != None:
                    out.append(lists[i].val)
                    lists[i] = lists[i].next
            if pre == len(out):
                break

        return sorted(out)




