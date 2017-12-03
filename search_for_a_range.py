# python3
# Given an array of integers sorted in ascending order,
# find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n).

# If the target is not found in the array, return [-1, -1].

# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].


# My solution
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def search_left(nums, l, r, target):
            if l >= r:
                return l
            mid = (l + r) // 2
            if nums[mid] >= target:
                return search_left(nums, l, mid, target)
            else:
                return search_left(nums, mid + 1, r, target)

        def search_right(nums, l, r, target):
            if l >= r:
                return l
            mid = (l + r) // 2
            if nums[mid] > target:
                return search_right(nums, l, mid, target)
            else:
                return search_right(nums, mid + 1, r, target)

        left = search_left(nums, 0, len(nums), target)
        right = search_right(nums, 0, len(nums), target)
        if left <= right - 1:
            return [left, right - 1]
        else:
            return [-1, -1]


