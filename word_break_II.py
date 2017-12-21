# python3
# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
# add spaces in s to construct a sentence where each word is a valid dictionary word.
# You may assume the dictionary does not contain duplicate words.

# Return all such possible sentences.

# For example, given
# s = "catsanddog",
# dict = ["cat", "cats", "and", "sand", "dog"].

# A solution is ["cats and dog", "cat sand dog"].


# My solution
class Solution(object):
    def wordBreak_one(self, s, wordDict):
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

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if not self.wordBreak_one(s, wordDict):
            return []

        dp = [False for _ in range(len(s))]
        for i in range(len(s)):
            for item in wordDict:
                if i - len(item) + 1 >= 0 and s[i - len(item) + 1:i + 1] == item:
                    if i - len(item) < 0:
                        dp[i] = [[item]]
                    elif dp[i - len(item)] != False:
                        if dp[i] != False:
                            dp[i].extend([it + [item] for it in dp[i - len(item)]])
                        else:
                            dp[i] = [it + [item] for it in dp[i - len(item)]]
        if dp[-1] == False:
            return []
        return [' '.join(it) for it in dp[-1]]
