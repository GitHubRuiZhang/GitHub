# python3
# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?

# For example,
# Given sorted array nums = [1,1,1,2,2,3],

# Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3.
# It doesn't matter what you leave beyond the new length.


# My solution
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        pre = None
        i = 0
        while i < len(nums):
            if nums[i] == pre:
                count += 1
                if count > 2:
                    nums.pop(i)
                else:
                    i += 1
            else:
                pre = nums[i]
                count = 1
                i += 1
        return len(nums)
