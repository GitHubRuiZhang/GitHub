# python3
# Given an encoded string, return it's decoded string.

# The encoding rule is: k[encoded_string],
# where the encoded_string inside the square brackets is being repeated exactly k times.
# Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

# Furthermore, you may assume that the original data does not contain any digits and that digits are only
# for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

# Examples:

# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".


# My solution
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        res = [[1, '']]
        count_bracket = 0
        cur_dig = ''
        cur_str = ''
        for i in range(len(s)):
            print(s[i], res, cur_dig, cur_str)
            if s[i] in digits:
                cur_dig += s[i]
            elif s[i] == '[':
                res.append([int(cur_dig), cur_str])
                cur_str = ''
                cur_dig = ''
            elif s[i] == ']':
                pre = res.pop()
                res[-1][1] += pre[0] * (pre[1] + cur_str)
            else:
                res[-1][1] += s[i]

        return res[0][1]



