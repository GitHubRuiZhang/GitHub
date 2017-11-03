# python3
# Given a sorted array consisting of only integers where every element appears twice except
# for one element which appears once. Find this single element that appears only once.

# Example 1:
# Input: [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:
# Input: [3,3,7,7,10,11,11]
# Output: 10
# Note: Your solution should run in O(log n) time and O(1) space.


# My solution
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def search(nums, l, r):
            if nums[r] != nums[r - 1]:
                return nums[r]
            if nums[l] != nums[l + 1]:
                return nums[l]
            mid = (l + r) // 2
            if mid % 2 == 1 and nums[mid] != nums[mid + 1]:
                return search(nums, mid - 1, r)
            elif mid % 2 == 1:
                return search(nums, l, mid - 1)
            elif mid % 2 == 0 and nums[mid] != nums[mid + 1]:
                return search(nums, l, mid)
            elif mid % 2 == 0:
                return search(nums, mid, r)

        return search(nums, 0, len(nums) - 1)

