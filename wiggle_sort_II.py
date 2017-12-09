# python3
# Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

# Example:
# (1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6].
# (2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].

# Note:
# You may assume all input has valid answer.

# Follow Up:
# Can you do it in O(n) time and/or in-place with O(1) extra space?


# My solution
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        res = sorted(nums)
        for i in range(len(nums) // 2):
            nums[i * 2] = res[(len(nums) - 1) // 2 - i]
            nums[i * 2 + 1] = res[len(nums) - i - 1]
        if len(nums) % 2 == 1:
            nums[-1] = res[0]



