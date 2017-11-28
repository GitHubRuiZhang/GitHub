# python3
# Given a sorted array, two integers k and x, find the k closest elements to x in the array.
# The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

# Example 1:
# Input: [1,2,3,4,5], k=4, x=3
# Output: [1,2,3,4]
# Example 2:
# Input: [1,2,3,4,5], k=4, x=-1
# Output: [1,2,3,4]
# Note:
# The value k is positive and will always be smaller than the length of the sorted array.
# Length of the given array is positive and will not exceed 104
# Absolute value of elements in the array and x will not exceed 104


# My solution
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

        def binary_search(arr, l, r, x):
            if l >= r:
                return l
            mid = (l + r) // 2
            if int(arr[mid]) >= x:
                return binary_search(arr, l, mid - 1, x)
            else:
                return binary_search(arr, mid + 1, r, x)

        index = binary_search(arr, 0, len(arr) - 1, x)
        out = []
        left = index
        right = index + 1
        while len(out) < k:
            if right >= len(arr) or (left >= 0 and (x - int(arr[left])) <= int(arr[right]) - x):
                out.append(int(arr[left]))
                left -= 1
            else:
                out.append(int(arr[right]))
                right += 1

        return sorted(out)



