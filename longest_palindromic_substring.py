# python3
# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example:

# Input: "babad"

# Output: "bab"

# Note: "aba" is also a valid answer.
# Example:

# Input: "cbbd"

# Output: "bb"


# My solution
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = 1
        out = (0, 1)
        dp = [[False for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s))[::-1]:
            dp[i][i] = True
            for j in range(i + 1, len(s)):
                if j == i + 1 and s[i] == s[j]:
                    dp[i][j] = True
                    if res < j - i + 1:
                        res = j - i + 1
                        out = (i, j + 1)
                elif j != i + 1 and s[j] == s[i] and dp[i + 1][j - 1] == True:
                    dp[i][j] = True
                    if res < j - i + 1:
                        res = j - i + 1
                        out = (i, j + 1)
        return s[out[0]:out[1]]



