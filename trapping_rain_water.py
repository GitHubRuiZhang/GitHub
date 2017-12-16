# python3
# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it is able to trap after raining.

# For example,
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


# My solution
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = []
        out = 0
        i = 0
        while i < len(height):
            while res and height[res[-1]] < height[i]:
                cur = res.pop()
                if res == []:
                    break
                out += (i - res[-1] - 1) * (min(height[i], height[res[-1]]) - height[cur])

            res.append(i)
            i += 1
        return out

        # naive
        out = 0
        height = [0] + height + [0]
        for i in range(1, len(height) - 1):
            left = max(height[:i])
            right = max(height[i + 1:])
            if left > height[i] and right > height[i]:
                out += min(left, right) - height[i]

        return out

