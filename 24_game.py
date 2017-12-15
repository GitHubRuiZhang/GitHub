# python3
# You have 4 cards each containing a number from 1 to 9. You need to judge whether
# they could operated through *, /, +, -, (, ) to get the value of 24.

# Example 1:
# Input: [4, 1, 8, 7]
# Output: True
# Explanation: (8-4) * (7-1) = 24
# Example 2:
# Input: [1, 2, 1, 2]
# Output: False
# Note:
# The division operator / represents real division, not integer division. For example, 4 / (1 - 2/3) = 12.
# Every operation done is between two numbers. In particular, we cannot use - as a unary operator.
# For example, with [1, 1, 1, 1] as input, the expression -1 - 1 - 1 - 1 is not allowed.
# You cannot concatenate numbers together. For example, if the input is [1, 2, 1, 2], we cannot write this as 12 + 12.


# My solution
class Solution(object):
    def solve(self, nums):
        if len(nums) == 0:
            return False
        elif len(nums) == 1:
            return abs(nums[0] - 24) < 1e-6

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    res = []
                    for k in range(len(nums)):
                        if k != i and k != j:
                            res.append(nums[k])
                    for k in range(4):
                        if k < 2 and j > i:
                            continue
                        if k == 0:
                            res.append(nums[i] + nums[j])
                        if k == 1:
                            res.append(nums[i] * nums[j])
                        if k == 2:
                            res.append(nums[i] - nums[j])
                        if k == 3:
                            if nums[j] != 0:
                                res.append(nums[i] / nums[j])
                            else:
                                continue
                        if self.solve(res):
                            return True
                        res.pop()
        return False

    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return self.solve(map(float, nums))

