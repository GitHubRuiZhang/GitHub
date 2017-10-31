# python3
# Given an integer array, you need to find one continuous subarray that if you only sort this subarray
# in ascending order, then the whole array will be sorted in ascending order, too.

# You need to find the shortest such subarray and output its length.


# Example 1:
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

# Note:
# Then length of the input array is in range [1, 10,000].
# The input array may contain duplicates, so ascending order here means <=.


# My solution
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_sorted = sorted(nums)
        diff_start = None
        for i in range(len(nums)):
            if nums_sorted[i] != nums[i]:
                diff_start = i
                break
        if diff_start == None:
            return 0
        diff_end = None
        for i in range(len(nums)):
            if nums_sorted[len(nums) - i - 1] != nums[len(nums) - i - 1]:
                diff_end = len(nums) - i - 1
                break
        return diff_end - diff_start + 1
