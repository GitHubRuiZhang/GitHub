# python3
# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

# Find all the elements that appear twice in this array.

# Could you do it without extra space and in O(n) runtime?

# Example:
# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [2,3]


# My solution
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        once = set(nums)
        twice = []
        for i in range(len(nums)):
            if nums[i] in once:
                once.remove(nums[i])
            else:
                twice.append(nums[i])
        return twice


# Another solution
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        out = []
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] < 0:
                out.append(abs(nums[i]))
            else:
                nums[abs(nums[i]) - 1] = -nums[abs(nums[i]) - 1]
        return out
