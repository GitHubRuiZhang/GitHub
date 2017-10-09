# python3
# Given two strings s and t which consist of only lowercase letters.

# String t is generated by random shuffling string s and then add one more letter at a random position.

# Find the letter that was added in t.

# Example:
# Input:
# s = "abcd"
# t = "abcde"
# Output:
# e

# Explanation:
# 'e' is the letter that was added.


# My solution
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        letters_s = sorted(list(s))
        letters_t = sorted(list(t))
        for i in range(len(s)):
            if letters_s[i] != letters_t[i]:
                return letters_t[i]

        return letters_t[-1]
