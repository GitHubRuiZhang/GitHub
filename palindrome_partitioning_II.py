# python3
# Given a string s, partition s such that every substring of the partition is a palindrome.

# Return the minimum cuts needed for a palindrome partitioning of s.

# For example, given s = "aab",
# Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.


# My solution
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == s[::-1]:
            return 0
        cur = [i for i in range(-1, len(s))]
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j] == s[j:i:-1]:
                    cur[j + 1] = min(cur[j + 1], cur[i] + 1)
        return cur[-1]
        # TLE
        dp = [[False for i in range(len(s))] for j in range(len(s))]
        for j in reversed(range(len(s))):
            dp[j][j] = True
            for i in range(j + 1, len(s)):
                if s[i] == s[j] and (i == j + 1 or dp[j + 1][i - 1] == True):
                    dp[j][i] = True

        def search(dp, s, start):
            out = len(s) - start
            for i in range(start, len(s)):
                if dp[start][i] == True:
                    child = search(dp, s, i + 1)
                    out = min(out, 1 + child)
            return out

        return search(dp, s, 0) - 1


