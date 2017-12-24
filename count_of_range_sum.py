# python3
# Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
# Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.

# Note:
# A naive algorithm of O(n2) is trivial. You MUST do better than that.

# Example:
# Given nums = [-2, 5, -1], lower = -2, upper = 2,
# Return 3.
# The three ranges are : [0, 0], [2, 2], [0, 2] and their respective sums are: -2, -1, 2.


# Solution
class Solution(object):
    def insideSort(self, l, r, lower, upper):
        mid = (l + r) / 2
        if mid == l:
            return 0
        cur = self.insideSort(l, mid, lower, upper) + self.insideSort(mid, r, lower, upper)
        i = j = mid
        for k in self.res[l:mid]:
            while i < r and self.res[i] - k < lower:
                i += 1
            while j < r and self.res[j] - k <= upper:
                j += 1
            cur += (j - i)
        self.res[l:r] = sorted(self.res[l:r])
        return cur

    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        self.res = [0]
        for it in nums:
            self.res.append(self.res[-1] + it)
        return self.insideSort(0, len(self.res), lower, upper)


