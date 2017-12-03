# python3
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.


# My solution
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
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
                if nums[mid] > target:
                    return bs(nums, l, mid, target)
                else:
                    return bs(nums, mid + 1, r, target)

        if nums == []:
            return -1
        out = bs(nums, 0, len(nums) - 1, target)
        if nums[out] == target:
            return out
        else:
            return -1

        # sort first
        def bs_normal(nums, l, r, target):
            if l >= r:
                return -1
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return bs_normal(nums, l, mid, target)
            else:
                return bs_normal(nums, mid + 1, r, target)

        if nums == []:
            return -1
        index = sorted(range(len(nums)), key=lambda x: nums[x])
        nums.sort()
        out = bs_normal(nums, 0, len(nums), target)
        if out == -1:
            return -1
        else:
            return index[out]
