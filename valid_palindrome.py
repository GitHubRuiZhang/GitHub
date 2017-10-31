# python3
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.

# Note:
# Have you consider that the string might be empty? This is a good question to ask during an interview.

# For the purpose of this problem, we define empty string as valid palindrome.


# My solution
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
            return True
        all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        i = 0
        j = len(s) - 1
        while i < len(s) // 2 and j > len(s) // 2 - 1:
            if s[i].lower() in all_letters and s[j].lower() in all_letters and s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            elif s[i].lower() in all_letters and s[j].lower() in all_letters:
                print('1')
                return False
            if s[i].lower() not in all_letters:
                i += 1
            if s[j].lower() not in all_letters:
                j -= 1

        return True
