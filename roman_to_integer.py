# python3
# Given a roman numeral, convert it to an integer.

# Input is guaranteed to be within the range from 1 to 3999.


# My solution
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        all_roman_letters = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        roman_to_integer = all_roman_letters[s[0]]
        for i in range(len(s) - 1):
            roman_to_integer += all_roman_letters[s[i + 1]]
            if all_roman_letters[s[i]] < all_roman_letters[s[i + 1]]:
                roman_to_integer -= 2 * all_roman_letters[s[i]]

        return roman_to_integer
