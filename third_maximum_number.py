# python3
# Given a non-empty array of integers, return the third maximum number in this array. If it does not exist,
# return the maximum number. The time complexity must be in O(n).

# Example 1:
# Input: [3, 2, 1]

# Output: 1

# Explanation: The third maximum is 1.
# Example 2:
# Input: [1, 2]

# Output: 2

# Explanation: The third maximum does not exist, so the maximum (2) is returned instead.

# Example 3:
# Input: [2, 2, 3, 1]

# Output: 1

# Explanation: Note that the third maximum here means the third maximum distinct number.
# Both numbers with value 2 are both considered as second maximum.


# My solution
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        three_max = []
        nums.sort()
        for num in nums:
            if three_max == []:
                three_max.append(num)
            elif num not in three_max:
                three_max.append(num)
                if len(three_max) > 3:
                    del three_max[0]
        return three_max[0] if len(three_max) == 3 else three_max[-1]

