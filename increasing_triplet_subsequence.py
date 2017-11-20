# python3
# Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

# Formally the function should:
# Return true if there exists i, j, k
# such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
# Your algorithm should run in O(n) time complexity and O(1) space complexity.

# Examples:
# Given [1, 2, 3, 4, 5],
# return true.

# Given [5, 4, 3, 2, 1],
# return false.


# My solution
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        """
        n1 = float('inf')
        n2 = float('inf')
        for i in range(len(nums)):
            if nums[i] < n1:
                n1 = nums[i]
            elif nums[i] > n1 and nums[i] < n2:
                n2 = nums[i]
            elif nums[i] > n2:
                return True
        return False

