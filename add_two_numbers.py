# python3
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


# My solution
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # solution2
        num1 = ''
        num2 = ''
        while l1:
            num1 = str(l1.val) + num1
            l1 = l1.next
        while l2:
            num2 = str(l2.val) + num2
            l2 = l2.next
        return map(int, reversed(list(str(int(num1) + int(num2)))))

        # solution1
        out = []
        pre = 0
        while l1 and l2:
            res = (l1.val + l2.val + pre)
            pre = res // 10
            res %= 10
            out.append(res)
            l1 = l1.next
            l2 = l2.next

        while l1:
            res = (l1.val + pre)
            pre = res // 10
            res %= 10
            out.append(res)
            l1 = l1.next

        while l2:
            res = (l2.val + pre)
            pre = res // 10
            res %= 10
            out.append(res)
            l2 = l2.next

        if pre != 0:
            out.append(pre)
        return out



