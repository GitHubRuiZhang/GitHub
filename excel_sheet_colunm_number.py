# python3
# Related to question Excel Sheet Column Title

# Given a column title as appear in an Excel sheet, return its corresponding column number.

# For example:

#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28


# My solution
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        output = 0
        all_titles = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        titles_to_numbers = {}
        for i in range(len(all_titles)):
            titles_to_numbers[all_titles[i]] = i
        for i in range(len(s)):
            output += (26**(i) *( titles_to_numbers[s[-i-1]] + 1) )
        return output