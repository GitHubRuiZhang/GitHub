# python3
# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

# The update(i, val) function modifies nums by updating the element at index i to val.
# Example:
# Given nums = [1, 3, 5]

# sumRange(0, 2) -> 9
# update(1, 2)
# sumRange(0, 2) -> 8
# Note:
# The array is only modifiable by the update function.
# You may assume the number of calls to update and sumRange function is distributed evenly.


# My solution
class Node(object):

    def __init__(self, l, r):
        self.val = 0
        self.l = l
        self.r = r
        self.left = None
        self.right = None


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """

        def build_tree(nums, l, r):
            if l > r:
                return None

            if l == r:
                node = Node(l, r)
                node.val = nums[l]
                return node

            mid = (l + r) // 2
            node = Node(l, r)
            node.left = build_tree(nums, l, mid)
            node.right = build_tree(nums, mid + 1, r)
            node.val = node.left.val + node.right.val

            return node

        self.root = build_tree(nums, 0, len(nums) - 1)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """

        def update_value(root, i, val):
            if root.l == root.r:
                root.val = val
                return val

            mid = (root.l + root.r) // 2

            if i <= mid:
                update_value(root.left, i, val)
            else:
                update_value(root.right, i, val)

            root.val = root.left.val + root.right.val

            return root.val

        return update_value(self.root, i, val)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """

        def sum_range(root, i, j):

            if root.l == i and root.r == j:
                return root.val

            mid = (root.l + root.r) // 2

            if j <= mid:
                return sum_range(root.left, i, j)
            elif i >= mid + 1:
                return sum_range(root.right, i, j)
            else:
                return sum_range(root.left, i, mid) + sum_range(root.right, mid + 1, j)

        return sum_range(self.root, i, j)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)