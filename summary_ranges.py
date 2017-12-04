# python3
# Given a sorted integer array without duplicates, return the summary of its ranges.

# Example 1:
# Input: [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Example 2:
# Input: [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]


# My solution
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        out = []
        start = None
        pre = None
        for i in range(len(nums)):
            if start == None:
                start = nums[i]
                pre = nums[i]
            elif nums[i] == pre + 1:
                pre = nums[i]
            elif nums[i] != pre + 1:
                if pre == start:
                    out.append(str(pre))
                else:
                    out.append(str(start) + '->' + str(pre))
                start = nums[i]
                pre = nums[i]

        if start != None and pre == start:
            out.append(str(pre))
        elif start != None:
            out.append(str(start) + '->' + str(pre))

        return out

