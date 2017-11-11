# python3
# Given an integer, convert it to a roman numeral.

# Input is guaranteed to be within the range from 1 to 3999.


# My solution
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return ""
        all_roman_letters = [[1000, 'M'], [500, 'D'], [100, 'C'], [50, 'L'], [10, 'X'], [5, 'V'], [1, 'I']]
        integer_to_roman = ""
        i = 0
        while i < 7:
            print(num, i)
            if i < 5 and i % 2 == 0 and num // all_roman_letters[i + 2][0] == 9:
                integer_to_roman += (all_roman_letters[i + 2][1] + all_roman_letters[i][1])
                num -= (9 * all_roman_letters[i + 2][0])
                i += 2
            elif i < 6 and i % 2 == 1 and num // all_roman_letters[i + 1][0] == 4:
                integer_to_roman += (all_roman_letters[i + 1][1] + all_roman_letters[i][1])
                num -= (4 * all_roman_letters[i + 1][0])
                i += 1
            elif num // all_roman_letters[i][0] > 0:
                integer_to_roman += (num // all_roman_letters[i][0]) * all_roman_letters[i][1]
                num -= (num // all_roman_letters[i][0] * all_roman_letters[i][0])
            else:
                i += 1

        return integer_to_roman



