# python3
# Given a positive integer, return its corresponding column title as appear in an Excel sheet.

# For example:

#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB


# My solution
# I spent a lot of time on 26//26 and 26%26
# I solved the problem with (n-1)//26 and (n-1)%26
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        all_titles = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                      'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        output = ''
        while n > 0:
            output = all_titles[(n - 1) % 26] + output
            n = (n - 1) // 26
        return output