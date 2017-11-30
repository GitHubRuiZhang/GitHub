# python3
# Given a string s, partition s such that every substring of the partition is a palindrome.

# Return all possible palindrome partitioning of s.

# For example, given s = "aab",
# Return

# [
#   ["aa","b"],
#   ["a","a","b"]
# ]


# My solution
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        dp = [[False for i in range(len(s))] for j in range(len(s))]
        for j in reversed(range(len(s))):
            dp[j][j] = True
            for i in range(j + 1, len(s)):
                if s[i] == s[j] and (i == j + 1 or dp[j + 1][i - 1] == True):
                    dp[j][i] = True

        def search(dp, s, start):
            out = []
            for i in range(start, len(s)):
                if dp[start][i] == True:
                    child = search(dp, s, i + 1)
                    if child == []:
                        out.append([s[start:i + 1]])
                    else:
                        out.extend([([s[start:i + 1]] + c) for c in child])
            return out

        return search(dp, s, 0)









