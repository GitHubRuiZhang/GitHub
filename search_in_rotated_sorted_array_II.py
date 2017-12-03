# python3
# Follow up for "Search in Rotated Sorted Array":
# What if duplicates are allowed?

# Would this affect the run-time complexity? How and why?
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

# Write a function to determine if a given target is in the array.

# The array may contain duplicates.


# My solution
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        def bs(nums, l, r, target):
            if l >= r:
                return l
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] < nums[l]:
                if target > nums[mid] and target < nums[l]:
                    return bs(nums, mid + 1, r, target)
                else:
                    return bs(nums, l, mid, target)
            elif nums[mid] > nums[r]:
                if target < nums[mid] and target > nums[r]:
                    return bs(nums, l, mid, target)
                else:
                    return bs(nums, mid + 1, r, target)
            else:
                # why -1? becasue of the duplicates, we cannot decide which side, so we can only decrease 1
                return bs(nums, l, r - 1, target)

        if nums == []:
            return False
        out = bs(nums, 0, len(nums) - 1, target)
        if nums[out] == target:
            return True
        else:
            return False