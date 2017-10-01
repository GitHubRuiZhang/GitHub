# python3
# You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2.
# Find all the next greater numbers for nums1's elements in the corresponding places of nums2.
# The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2.
# If it does not exist, output -1 for this number.

# Example:
# Input:
# nums1 = [4,1,2],
# nums2 = [1,3,4,2].
# Output:
# [-1,3,-1]
# Explanation:
# For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
# For number 1 in the first array, the next greater number for it in the second array is 3.
# For number 2 in the first array, there is no next greater number for it in the second array, so output -1.

# Example:
# Input:
# nums1 = [2,4],
# nums2 = [1,2,3,4].
# Output:
# [3,-1]
# Explanation:
# For number 2 in the first array, the next greater number for it in the second array is 3.
# For number 4 in the first array, there is no next greater number for it in the second array, so output -1.


# My solution
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        nextGreaterNumber = [-1 for _ in range(len(nums))]
        uncomparedNumber = []
        findNumsDic = {}
        for i in range(len(nums)):
            # compare uncompard numbers
            j = 0
            while j < len(uncomparedNumber):
                if nums[i] > nums[uncomparedNumber[j]]:
                    nextGreaterNumber[uncomparedNumber[j]] = nums[i]
                    del uncomparedNumber[j]
                else:
                    j += 1

            # index of uncompared numbers
            uncomparedNumber.append(i)
            # map numbers to their indexes
            findNumsDic[nums[i]] = i

        output = []
        for i in range(len(findNums)):
            output.append(nextGreaterNumber[findNumsDic[findNums[i]]])

        return output