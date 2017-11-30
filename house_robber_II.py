# python3
# Note: This is an extension of House Robber.

# After robbing those houses on that street,
# the thief has found himself a new place for his thievery so that he will not get too much attention.
# This time, all houses at this place are arranged in a circle.
# That means the first house is the neighbor of the last one.
# Meanwhile, the security system for these houses remain the same as for those in the previous street.

# Given a list of non-negative integers representing the amount of money of each house,
# determine the maximum amount of money you can rob tonight without alerting the police.


# My solution
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        max_up_to = [nums[0], max(nums[0], nums[1])]
        max_up_to_no1 = [0, nums[1]]
        for i in range(2, len(nums) - 1):
            max_up_to.append(max(max_up_to[i - 1], max_up_to[i - 2] + nums[i]))
            max_up_to_no1.append(max(max_up_to_no1[i - 1], max_up_to_no1[i - 2] + nums[i]))

        return max(max_up_to_no1[-2] + nums[-1], max_up_to[-1])
