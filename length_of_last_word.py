# python3
# Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
# return the length of last word in the string.

# If the last word does not exist, return 0.

# Note: A word is defined as a character sequence consists of non-space characters only.

# For example,
# Given s = "Hello World",
# return 5.


# My solution
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        exist = False
        for i in range(len(s)):
            if exist and s[-1 - i] == ' ':
                break
            elif exist:
                length += 1
            elif not exist and s[-1 - i] != ' ':
                length += 1
                exist = True

        return length
