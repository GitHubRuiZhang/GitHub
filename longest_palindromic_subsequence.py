# python3
# Given a string s, find the longest palindromic subsequence's length in s.
# You may assume that the maximum length of s is 1000.

# Example 1:
# Input:

# "bbbab"
# Output:
# 4
# One possible longest palindromic subsequence is "bbbb".
# Example 2:
# Input:

# "cbbd"
# Output:
# 2
# One possible longest palindromic subsequence is "bb".


# My solution
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == s[::-1]:
            return len(s)
        dp = [[0 for j in range(len(s))] for i in range(len(s))]
        for i in reversed(range(len(s))):
            dp[i][i] = 1
            for j in range(i+1,len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][(j - 1)] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][(j - 1)])
        return dp[0][-1]


