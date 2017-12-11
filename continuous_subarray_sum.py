# python3
# Given a list of non-negative numbers and a target integer k,
# write a function to check if the array has a continuous subarray of size at least 2 that sums up to the multiple of k,
# that is, sums up to n*k where n is also an integer.

# Example 1:
# Input: [23, 2, 4, 6, 7],  k=6
# Output: True
# Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
# Example 2:
# Input: [23, 2, 6, 4, 7],  k=6
# Output: True
# Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
# Note:
# The length of the array won't exceed 10,000.
# You may assume the sum of all the numbers is in the range of a signed 32-bit integer.


# My solution
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 0:
            pre = None
            for i in range(len(nums)):
                if nums[i] == 0 and pre == 0:
                    return True
                pre = nums[i]
            return False

        k = abs(k)
        if len(nums) >= 2 * k:
            return True

        all_num = [0]
        for i in range(len(nums)):
            all_num.append((all_num[-1] + nums[i]) % k)

        num_pos = {}
        for i in range(len(all_num)):
            if all_num[i] in num_pos:
                if i - num_pos[all_num[i]] > 1:
                    return True
            else:
                num_pos[all_num[i]] = i

        return False


