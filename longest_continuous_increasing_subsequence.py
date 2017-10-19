# python3
# Given an unsorted array of integers, find the length of longest continuous increasing subsequence.

# Example 1:
# Input: [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3.
# Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4.

# Example 2:
# Input: [2,2,2,2,2]
# Output: 1
# Explanation: The longest continuous increasing subsequence is [2], its length is 1.


# My solution
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = 0
        start = 0
        current = float('inf')
        for num in nums:
            if start == 0 or current < num:
                start += 1
            else:
                length = max(length, start)
                start = 1
            current = num

        return max(length, start)