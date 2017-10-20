# python3
# We define a harmonious array is an array where the difference between its maximum value
# and its minimum value is exactly 1.

# Now, given an integer array, you need to find the length of its longest harmonious
# subsequence among all its possible subsequences.

# Example 1:
# Input: [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].
# Note: The length of the input array will not exceed 20,000.


# My solution
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        out = 0
        nums.sort()
        nums_dict = []
        pre = nums[0]
        pre_count = -1  # start with -1 to operate the first number
        for i in range(len(nums)):
            if nums[i] != pre:
                nums_dict.append([pre, i - 1 - pre_count])
                pre = nums[i]
                pre_count = i - 1
                if len(nums_dict) > 1 and nums_dict[-1][0] - nums_dict[-2][0] == 1:
                    out = max(out, nums_dict[-1][1] + nums_dict[-2][1])
        nums_dict.append([nums[i], i - pre_count])
        if len(nums_dict) > 1 and nums_dict[-1][0] - nums_dict[-2][0] == 1:
            out = max(out, nums_dict[-1][1] + nums_dict[-2][1])
        return out
