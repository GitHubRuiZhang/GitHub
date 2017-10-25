# python3
# Count the number of segments in a string,
# where a segment is defined to be a contiguous sequence of non-space characters.

# Please note that the string does not contain any non-printable characters.

# Example:

# Input: "Hello, my name is John"
# Output: 5


# My solution
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        count = 0
        s += ' '
        for i in range(len(s)):
            if s[i] != ' ' and s[i+1] == ' ':
                count += 1
        return count
