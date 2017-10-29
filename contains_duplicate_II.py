# python3
# Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array
# such that nums[i] = nums[j] and the absolute difference between i and j is at most k.


# My solution
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) - 1 <= k:
            return len(set(nums)) < len(nums)
        window = set()
        pre = 0
        for i in range(len(nums)):
            if i <= k:
                if nums[i] in window:
                    return True
                else:
                    window.add(nums[i])
            else:
                window.remove(nums[pre])
                if nums[i] in window:
                    return True
                else:
                    window.add(nums[i])
                pre += 1
        return False

