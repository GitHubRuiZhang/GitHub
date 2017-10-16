# python3
# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.


# My solution
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        str_position = {}
        for i in range(len(s)):
            if s[i] not in str_position:
                str_position[s[i]] = i
            else:
                str_position[s[i]] = -1

        output = -1
        for sp in str_position.items():
            if sp[1] != -1 and output == -1:
                output = sp[1]
            elif sp[1] != -1 and output > sp[1]:
                output = sp[1]

        return output