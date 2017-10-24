# python3
# Write a function that takes a string as input and reverse only the vowels of a string.

# Example 1:
# Given s = "hello", return "holle".

# Example 2:
# Given s = "leetcode", return "leotcede".

# Note:
# The vowels does not include the letter "y".


# My solution
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        list_vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        pos = []
        vow = ''
        new_s = []
        for i in range(len(s)):
            new_s.append(str(s[i]))
            if s[i] in list_vowels:
                vow = str(s[i]) + vow
                pos.append(i)
        for j in range(len(pos)):
            new_s[pos[j]] = vow[j]

        return ''.join(new_s)


# My solution
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        list_vowels = ['a', 'e', 'i', 'o', 'u']
        new_s = [l for l in s]
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i].lower() in list_vowels and s[j].lower() in list_vowels:
                new_s[i], new_s[j] = new_s[j], new_s[i]
                j -= 1
                i += 1
            elif s[i].lower() in list_vowels:
                j -= 1
            elif s[j].lower() in list_vowels:
                i += 1
            else:
                j -= 1
                i += 1

        return ''.join(new_s)