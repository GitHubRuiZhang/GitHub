# python3
# Given a non-negative integer, you could swap two digits at most once to get the maximum valued number.
# Return the maximum valued number you could get.

# Example 1:
# Input: 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
# Example 2:
# Input: 9973
# Output: 9973
# Explanation: No swap.
# Note:
# The given number is in the range [0, 108]


# My solution
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_str = list(str(num))
        cur = num
        for i in range(len(num_str) - 1):
            res = num_str[i]
            pos = None
            for j in range(i + 1, len(num_str)):
                if res <= num_str[j]:
                    res = num_str[j]
                    pos = j
            if pos is not None:
                num_str[i], num_str[pos] = num_str[pos], num_str[i]
                cur = max(int("".join(num_str)), cur)
                num_str = list(str(num))
        return cur








