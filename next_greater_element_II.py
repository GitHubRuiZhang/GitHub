# python3
# Given a circular array (the next element of the last element is the first element of the array),
# print the Next Greater Number for every element.
# The Next Greater Number of a number x is the first greater number to its traversing-order next in the array,
#  which means you could search circularly to find its next greater number.
# If it doesn't exist, output -1 for this number.

# Example 1:
# Input: [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2;
# The number 2 can't find next greater number;
# The second 1's next greater number needs to search circularly, which is also 2.
# Note: The length of given array won't exceed 10000.


# My solution
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        out = [-1 for _ in range(len(nums))]
        find = []
        for i in range(len(nums)) * 2:
            while find and (nums[find[-1]] < nums[i]):
                out[find.pop()] = nums[i]
            find.append(i)

        return out

