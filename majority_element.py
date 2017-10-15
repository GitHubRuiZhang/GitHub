# python3
# Given an array of size n, find the majority element.
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.


# My solution
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_times = {}
        for num in nums:
            if num in nums_times:
                nums_times[num] += 1
            else:
                nums_times[num] = 1
            if nums_times[num] > len(nums) // 2:
                return num

        return False