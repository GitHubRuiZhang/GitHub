# python3
# A linked list is given such that each node contains an additional random pointer
# which could point to any node in the list or null.

# Return a deep copy of the list.


# My solution
# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        all_nodes = {}
        node1 = head
        node2 = head
        while node1:
            all_nodes[node1] = RandomListNode(node1.label)
            node1 = node1.next
        while node2:
            all_nodes[node2].next = all_nodes.get(node2.next)
            all_nodes[node2].random = all_nodes.get(node2.random)
            node2 = node2.next
        return all_nodes.get(head)
