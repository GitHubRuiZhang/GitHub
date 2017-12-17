# python3
# Given a string containing just the characters '(' and ')',
# find the length of the longest valid (well-formed) parentheses substring.

# For "(()", the longest valid parentheses substring is "()", which has length = 2.

# Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.


# My solution
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        out = 0
        if s == '':
            return 0
        dp = [0 for _ in range(len(s))]
        for i in range(len(s)):
            if s[i] == ')' and i - 1 >= 0 and s[i - 1] == '(':
                if i - 2 >= 0:
                    dp[i] = dp[i - 2] + 2
                else:
                    dp[i] = 2
            elif s[i] == ')' and i - 1 >= 0 and s[i - 1] == ')':
                cur = i - dp[i - 1] - 1
                if cur >= 0 and s[cur] == '(':
                    if cur - 1 >= 0:
                        dp[i] = dp[i - 1] + dp[cur - 1] + 2
                    else:
                        dp[i] = dp[i - 1] + 2
            out = max(out, dp[i])

        return out

