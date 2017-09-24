# python3
# Given a string, you need to reverse the order of
# characters in each word within a sentence while still preserving whitespace and initial word order.

# Example:
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

# My solution
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_words = s.split()
        return ' '.join(it[::-1] for it in s_words)