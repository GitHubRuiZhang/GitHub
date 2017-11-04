# python3
# Given a string, your task is to count how many palindromic substrings in this string.

# The substrings with different start indexes or end indexes are counted as different substrings
# even they consist of same characters.

# Example 1:
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# Example 2:
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
# Note:
# The input string length won't exceed 1000.


# My solution
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        def palindromic(s):
            s_inverse = s[::-1]
            if s == s_inverse:
                return True
            else:
                return False

        current = len(s)
        count = 0
        while current > 0:
            for i in range(len(s) - current + 1):
                if palindromic(s[i:i + current]) == True:
                    count += 1

            current -= 1
        return count
