# python3
# Implement wildcard pattern matching with support for '?' and '*'.

# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).

# The matching should cover the entire input string (not partial).

# The function prototype should be:
# bool isMatch(const char *s, const char *p)

# Some examples:
# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "*") → true
# isMatch("aa", "a*") → true
# isMatch("ab", "?*") → true
# isMatch("aab", "c*a*b") → false


# My solution
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n = len(s)
        if len(p) - p.count('*') > n:
            return False
        dp = [False for _ in range(n+1)]
        dp[0] = True
        for it in p:
            if it != '*':
                for i in reversed(range(n)):
                    dp[i+1] = dp[i] and (it == s[i] or it == '?')
            else:
                for i in range(n):
                    dp[i+1] = dp[i] or dp[i+1]
            dp[0] = dp[0] and it == '*'
        return dp[-1]