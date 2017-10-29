# python3
# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

# Example 1:
# Input: "aba"
# Output: True
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# Note:
# The string will only contain lowercase characters a-z. The maximum length of the string is 50000.


# My solution
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1
        while i < len(s) // 2 and j > len(s) // 2 - 1:
            if s[i] != s[j]:
                s_i = s[:i] + s[i + 1:]
                s_j = s[:j] + s[j + 1:]
                if s_i[::-1] == s_i or s_j[::-1] == s_j:
                    return True
                else:
                    return False
            else:
                i += 1
                j -= 1

        return True
