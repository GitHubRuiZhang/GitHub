# python3
# Given a non-negative integer represented as a non-empty array of digits,
# plus one to the integer.

# You may assume the integer do not contain any leading zero,
# except the number 0 itself.

# The digits are stored such that the most significant digit is at the head of the list.


# My solution
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits == []:
            return []
        i = len(digits) - 1
        digits[i] += 1
        while digits[i] == 10:
            digits[i] = 0
            i -= 1
            if i < 0:
                digits.insert(0, 1)
                break
            digits[i] += 1

        return digits