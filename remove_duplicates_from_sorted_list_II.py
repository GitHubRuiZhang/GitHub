# python3
# Given a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list.

# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.


# My solution
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = {}
        parent = {}
        node = head
        parent[head] = None
        pre = None
        while node:
            if node.val in res:
                res[node.val].append(node)
                while res[node.val]:
                    it = res[node.val].pop(0)
                    if head == it:
                        head = it.next
                        parent[head] = None
                    else:
                        parent[it].next = it.next
                        parent[it.next] = parent[it]
                pre = parent[it]
                node = it.next
            else:
                res[node.val] = [node]
                parent[node] = pre
                pre = node
                node = node.next

        return head
