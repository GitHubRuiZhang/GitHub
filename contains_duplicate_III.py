# python3
# Given an array of integers,
# find out whether there are two distinct indices i and j in the array such that the absolute difference
# between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.


# My solution
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        res = {}
        for i in range(len(nums)):
            cur = nums[i] // t if t else nums[i]
            if cur in res and abs(nums[i] - res[cur]) <= t:
                return True
            if t != 0 and cur - 1 in res and abs(nums[i] - res[cur - 1]) <= t:
                return True
            if t != 0 and cur + 1 in res and abs(nums[i] - res[cur + 1]) <= t:
                return True
            res[cur] = nums[i]
            if len(res) > k:
                del res[(nums[i - k] // t) if t else nums[i - k]]

        return False

        # naive
        nums_index = sorted(range(len(nums)), key=lambda x: nums[x])
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] - nums[i] <= t and abs(nums_index[j] - nums_index[i]) <= k:
                    return True
        return False




