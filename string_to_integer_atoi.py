# python3
# Implement atoi to convert a string to an integer.

# Hint: Carefully consider all possible input cases.
# If you want a challenge, please do not see below and ask yourself what are the possible input cases.

# Notes: It is intended for this problem to be specified vaguely (ie, no given input specs).
# You are responsible to gather all the input requirements up front.

# Update (2015-02-10):
# The signature of the C++ function had been updated.
# If you still see your function signature accepts a const char * argument,
# please click the reload button  to reset your code definition.

# spoilers alert... click to show requirements for atoi.

# Requirements for atoi:
# The function first discards as many whitespace characters as necessary
# until the first non-whitespace character is found.
# Then, starting from this character,
# takes an optional initial plus or minus sign followed by as many numerical digits as possible,
# and interprets them as a numerical value.

# The string can contain additional characters after those that form the integral number,
# which are ignored and have no effect on the behavior of this function.

# If the first sequence of non-whitespace characters in str is not a valid integral number,
# or if no such sequence exists because either str is empty or it contains only whitespace characters,
# no conversion is performed.

# If no valid conversion could be performed, a zero value is returned.
# If the correct value is out of the range of representable values,
# INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.


# My solution
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        i = 0
        count1 = 0
        count2 = 0
        res = '0123456789'
        while i < len(str):
            if str[i] == ' ' and str[:i] == '' and count1 == 0 and count2 == 0:
                str = str[:i] + str[i + 1:]
            elif str[i] == ' ':
                str = str[:i]
                break
            elif str[i] == '+':
                count1 += 1
                str = str[:i] + str[i + 1:]
            elif str[i] == '-':
                count2 += 1
                str = str[:i] + str[i + 1:]
            elif str[i] in res:
                i += 1
            else:
                str = str[:i]
                break
            print(str)
        if str == '':
            return 0
        sign = count1 - count2
        try:
            if (count1 != 0 and count2 != 0 and sign == 0) or (count1 > 1) or (count2 > 1):
                return 0
            elif sign < 0:
                if int(str) > 2147483648:
                    return -2147483648
                return -int(str)
            else:
                if int(str) > 2147483647:
                    return 2147483647
                return int(str)
        except:
            return str
