# python3
# In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.

# Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.

# Return the result as a list of indices representing the starting position of each interval (0-indexed).
# If there are multiple answers, return the lexicographically smallest one.

# Example:
# Input: [1,2,1,2,6,7,5,1], 2
# Output: [0, 3, 5]
# Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
# We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
# Note:
# nums.length will be between 1 and 20000.
# nums[i] will be between 1 and 65535.
# k will be between 1 and floor(nums.length / 3).


# My solution
class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        index1 = [0]
        index2 = [0, k]
        index3 = [0, k, k * 2]

        sum1 = sum(nums[:k])
        sum2 = sum(nums[k:2 * k])
        sum3 = sum(nums[k * 2:k * 3])

        best1 = sum1
        best2 = sum1 + sum2
        best3 = sum1 + sum2 + sum3

        cur1 = 1
        cur2 = k + 1
        cur3 = k * 2 + 1
        while cur3 <= len(nums) - k:
            sum1 = sum1 - nums[cur1 - 1] + nums[cur1 + k - 1]
            sum2 = sum2 - nums[cur2 - 1] + nums[cur2 + k - 1]
            sum3 = sum3 - nums[cur3 - 1] + nums[cur3 + k - 1]

            if sum1 > best1:
                best1 = sum1
                index1 = [cur1]

            if best1 + sum2 > best2:
                best2 = best1 + sum2
                index2 = index1 + [cur2]

            if best2 + sum3 > best3:
                best3 = best2 + sum3
                index3 = index2 + [cur3]

            cur1 += 1
            cur2 += 1
            cur3 += 1
        return index3
