# python3
# Given a word, you need to judge whether the usage of capitals in it is right or not.

# We define the usage of capitals in a word to be right when one of the following cases holds:

# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital if it has more than one letter, like "Google".
# Otherwise, we define that this word doesn't use capitals in a right way.
# Example 1:
# Input: "USA"
# Output: True
# Example 2:
# Input: "FlaG"
# Output: False
# Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.


# My solution
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        all_uppercase_letters = set(
            ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X',
             'C', 'V', 'B', 'N', 'M'])

        num_upper_letters = 0
        if word[0] in all_uppercase_letters:
            start_upper = True
            num_upper_letters += 1
        else:
            start_upper = False

        for letter in word[1:]:
            if letter in all_uppercase_letters:
                num_upper_letters += 1
                if not start_upper:
                    return False

        possible_outcomes = set([1, len(word)])
        if start_upper and num_upper_letters not in possible_outcomes:
            return False

        return True

    