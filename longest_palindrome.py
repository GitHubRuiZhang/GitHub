# python3
# Given a string which consists of lowercase or uppercase letters,
# find the length of the longest palindromes that can be built with those letters.

# This is case sensitive, for example "Aa" is not considered a palindrome here.

# Note:
# Assume the length of given string will not exceed 1,010.

# Example:

# Input:
# "abccccdd"

# Output:
# 7

# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.


# My solution
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_set = set()
        num = 0
        for letter in s:
            if letter not in s_set:
                s_set.add(letter)
            else:
                s_set.remove(letter)
                num += 2

        if num < len(s):
            num += 1

        return num
