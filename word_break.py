# python3
# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
# determine if s can be segmented into a space-separated sequence of one or more dictionary words.
# You may assume the dictionary does not contain duplicate words.

# For example, given
# s = "leetcode",
# dict = ["leet", "code"].

# Return true because "leetcode" can be segmented as "leet code".

# UPDATE (2017/1/4):
# The wordDict parameter had been changed to a list of strings (instead of a set of strings).
# Please reload the code definition to get the latest changes.


# My solution
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False for _ in range(len(s))]
        for i in range(len(s)):
            for item in wordDict:
                if i - len(item) + 1 >= 0 and s[i - len(item) + 1:i + 1] == item and (
                        i - len(item) < 0 or dp[i - len(item)] == True):
                    dp[i] = True
        return dp[-1]

