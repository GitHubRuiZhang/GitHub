# python3
# Given an array with n integers,
# your task is to check if it could become non-decreasing by modifying at most 1 element.

# We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

# Example 1:
# Input: [4,2,3]
# Output: True
# Explanation: You could modify the first
# 4
#  to
# 1
#  to get a non-decreasing array.
# Example 2:
# Input: [4,2,1]
# Output: False
# Explanation: You can't get a non-decreasing array by modify at most one element.
# Note: The n belongs to [1, 10,000].


# My solution
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        pre = -float('inf')
        pre_pre = -float('inf')
        for i in range(len(nums)):
            if nums[i] < pre:
                count += 1
                if count > 1:
                    return False
                if nums[i] < pre_pre:
                    continue
                elif i + 1 < len(nums) and nums[i + 1] < pre:
                    pre = nums[i]
            else:
                pre_pre = pre
                pre = nums[i]

        return True

