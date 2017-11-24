# python3
# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.

# Note: You may not slant the container and n is at least 2.


# My solution
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Naive
        # out = 0
        # for i in range(len(height)):
        #     for j in range(i+1,len(height)):
        #         out = max(out, min(height[i],height[j])*(j-i))
        # return out

        i = 0
        j = len(height) - 1
        out = 0
        while i < j:
            if height[i] < height[j]:
                out = max(out, height[i] * (j - i))
                i += 1
            else:
                out = max(out, height[j] * (j - i))
                j -= 1
        return out
