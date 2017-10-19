# python3
# Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting
# from the start of the string. If there are less than k characters left, reverse all of them.
# If there are less than 2k but greater than or equal to k characters,
# then reverse the first k characters and left the other as original.

# Example:
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# Restrictions:
# The string consists of lower English letters only.
# Length of the given string and k will in the range [1, 10000]


# My solution
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if len(s)//k == 0:
            return s[::-1]
        i = 0
        while i < (len(s)//k):
            if i % 2 == 0:
                reverse = s[i*k:(i+1)*k]
                reverse = reverse[::-1]
                s = s[:i*k] + reverse +s[(i+1)*k:]
            i += 1
        if i % 2 == 0 and i*k <= len(s) - 1:
            reverse = s[i*k:]
            reverse = reverse[::-1]
            s = s[:i*k] + reverse
        return s
