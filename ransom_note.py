# python3
# Given an arbitrary ransom note string and another string containing letters from all the magazines,
# write a function that will return true if the ransom note can be constructed from the magazines ;
# otherwise, it will return false.

# Each letter in the magazine string can only be used once in your ransom note.

# Note:
# You may assume that both strings contain only lowercase letters.

# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true


# My solution
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        all_letters = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0,
                       'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0,
                       'y': 0, 'z': 0}
        for letter in magazine:
            all_letters[letter] += 1

        for letter in ransomNote:
            all_letters[letter] -= 1
            if all_letters[letter] < 0:
                return False

        return True


# Another one
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        all_letters = {}
        for letter in magazine:
            if letter in all_letters:
                all_letters[letter] += 1
            else:
                all_letters[letter] = 1

        for letter in ransomNote:
            if letter not in all_letters:
                return False
            all_letters[letter] -= 1
            if all_letters[letter] < 0:
                return False

        return True