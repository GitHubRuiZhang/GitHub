# python3
# Rotate an array of n elements to the right by k steps.

# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

# Note:
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.


# My solution I
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        while k>0:
            nums.insert(0,nums.pop())
            k -= 1


# My solution II
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums[(len(nums)-k):] + nums[:(len(nums)-k)]
        # Cant be written as nums_new = nums[(len(nums)-k):] + nums[:(len(nums)-k)]


# My solution III
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        while k > len(nums):
            k = k - len(nums)
        count = len(nums) - k
        while count > 0:
            nums.append(nums.pop(0))
            count -= 1
