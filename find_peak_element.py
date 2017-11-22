# python3
# A peak element is an element that is greater than its neighbors.

# Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

# You may imagine that num[-1] = num[n] = -∞.

# For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.


# My solution
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def binary_search(nums, l, r):
            if l >= r:
                return l
            mid = (l + r) // 2
            if nums[mid] < nums[mid + 1]:
                return binary_search(nums, mid + 1, r)
            else:
                return binary_search(nums, l, mid)

        return binary_search(nums, 0, len(nums) - 1)
