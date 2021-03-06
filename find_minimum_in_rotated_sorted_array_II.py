# python3
# Follow up for "Find Minimum in Rotated Sorted Array":
# What if duplicates are allowed?

# Would this affect the run-time complexity? How and why?
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

# Find the minimum element.

# The array may contain duplicates.


# My solution
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def search(nums, l, r):
            if l >= r:
                return nums[l]
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
            return search(nums, l, r)

        s = 0
        e = len(nums) - 1
        while nums[s] == nums[e] and s < e:
            e -= 1
        return search(nums, s, e)


