# python3
# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# Example 1:
# nums1 = [1, 3]
# nums2 = [2]

# The median is 2.0
# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5


# My solution
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m

        l, r, res = 0, m, (m + n + 1) / 2
        while l <= r:
            mid = (l + r) / 2
            cur = res - mid
            if mid < m and nums2[cur - 1] > nums1[mid]:
                l += 1
            elif mid > 0 and nums1[mid - 1] > nums2[cur]:
                r -= 1
            else:
                if mid == 0:
                    left = nums2[cur - 1]
                elif cur == 0:
                    left = nums1[mid - 1]
                else:
                    left = max(nums1[mid - 1], nums2[cur - 1])

                if (m + n) % 2 == 1:
                    return left

                if mid == m:
                    left1 = nums2[cur]
                elif cur == n:
                    left1 = nums1[mid]
                else:
                    left1 = min(nums1[mid], nums2[cur])

                return (left + left1) / 2.0


