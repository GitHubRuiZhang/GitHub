# python3
# Given an array consists of non-negative integers,
# your task is to count the number of triplets chosen from the array that can make triangles
# if we take them as side lengths of a triangle.

# Example 1:
# Input: [2,2,3,4]
# Output: 3
# Explanation:
# Valid combinations are:
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3
# Note:
# The length of the given array won't exceed 1000.
# The integers in the given array are in the range of [0, 1000].


# My solution
class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def binary_search(nums, l, r, target):
            while r >= l and r < len(nums):
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return l

        nums.sort()
        k = 1
        count = 0
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                cur = nums[i] + nums[j]
                k = binary_search(nums, j + 1, len(nums) - 1, cur)
                count += (k - j - 1)

        return count