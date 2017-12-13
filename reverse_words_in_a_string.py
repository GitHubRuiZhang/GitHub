# python3
# Given an input string, reverse the string word by word.

# For example,
# Given s = "the sky is blue",
# return "blue is sky the".

# Update (2015-02-12):
# For C programmers: Try to solve it in-place in O(1) space.

# click to show clarification.

# Clarification:
# What constitutes a word?
# A sequence of non-space characters constitutes a word.
# Could the input string contain leading or trailing spaces?
# Yes. However, your reversed string should not contain leading or trailing spaces.
# How about multiple spaces between two words?
# Reduce them to a single space in the reversed string.


# My solution
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = s.split(' ')
        j = 0
        while j < len(res):
            i = 0
            while i < len(res[j]):
                if res[j][i] == ' ':
                    res[j] = res[j][:i] + res[j][i + 1:]
                else:
                    i += 1
            if res[j] == '':
                res.pop(j)
            else:
                j += 1

        res = res[::-1]
        return ' '.join(res)
