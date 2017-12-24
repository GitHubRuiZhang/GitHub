# python3
# Given two arrays of length m and n with digits 0-9 representing two numbers.
# Create the maximum number of length k <= m + n from digits of the two.
# The relative order of the digits from the same array must be preserved. Return an array of the k digits.
# You should try to optimize your time and space complexity.

# Example 1:
# nums1 = [3, 4, 6, 5]
# nums2 = [9, 1, 2, 5, 8, 3]
# k = 5
# return [9, 8, 6, 5, 3]

# Example 2:
# nums1 = [6, 7]
# nums2 = [6, 0, 4]
# k = 5
# return [6, 7, 6, 0, 4]

# Example 3:
# nums1 = [3, 9]
# nums2 = [8, 9]
# k = 3
# return [9, 8, 9]


# Solution
class Solution(object):
    def find(self, nums, index):
        res = [-1]
        if index > len(nums):
            return res
        while index > 0:
            l = res[-1] + 1
            r = len(nums) - index + 1
            res.append(max(range(l, r), key=nums.__getitem__))
            index -= 1
        res = [nums[it] for it in res[1:]]
        return res

    def merge(self, nums1, nums2):
        out = []
        while nums1 or nums2:
            if nums1 > nums2:
                out.append(nums1.pop(0))
            else:
                out.append(nums2.pop(0))
        return out

    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = [0 for _ in range(k)]
        for i in range(k + 1):
            j = k - i
            if i > len(nums1) or j > len(nums2):
                continue
            left = self.find(nums1, i)
            right = self.find(nums2, j)
            num = self.merge(left, right)
            res = max(num, res)
        return res
