# python3
# Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of
# the substring together. You may assume the given string consists of lowercase English letters only
# and its length will not exceed 10000.

# Example 1:
# Input: "abab"

# Output: True

# Explanation: It's the substring "ab" twice.
# Example 2:
# Input: "aba"

# Output: False
# Example 3:
# Input: "abcabcabcabc"

# Output: True

# Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)


# My solution
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
            return True
        sub_start = [s[0]]
        for i in range(1, len(s) // 2 + 1):
            if s[i] == s[0] and len(s) % i == 0:
                Judge = True
                for j in range(1, len(s) / i):
                    if s[j * i:(j + 1) * i] != s[:i]:
                        Judge = False
                        break
                else:
                    return True

        return False
