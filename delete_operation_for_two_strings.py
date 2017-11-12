# python3
# Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same,
# where in each step you can delete one character in either string.

# Example 1:
# Input: "sea", "eat"
# Output: 2
# Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

# Note:
# The length of given words won't exceed 500.
# Characters in given words can only be lower-case letters.


# My solution
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[0 for j in range(len(word1) + 1)] for i in range(len(word2) + 1)]
        for i in range(len(word2)):
            for j in range(len(word1)):
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i][j] + (word1[j] == word2[i]), dp[i + 1][j])

        return len(word1) + len(word2) - 2 * dp[-1][-1]
