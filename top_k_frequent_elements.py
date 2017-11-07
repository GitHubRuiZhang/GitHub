# python3
# Given a non-empty array of integers, return the k most frequent elements.

# For example,
# Given [1,1,1,2,2,3] and k = 2, return [1,2].

# Note:
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


# My solution
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict_nums = {}
        all_frequencies = [[] for _ in range(len(nums) + 1)]
        for i in range(len(nums)):
            if nums[i] in dict_nums:
                all_frequencies[dict_nums[nums[i]]].remove(nums[i])
                dict_nums[nums[i]] += 1
            else:
                dict_nums[nums[i]] = 1
            all_frequencies[dict_nums[nums[i]]].append(nums[i])
        out = []
        for i in range(len(nums) + 1):
            if len(out) >= k:
                break
            else:
                out.extend(all_frequencies[-i - 1])
        return out

