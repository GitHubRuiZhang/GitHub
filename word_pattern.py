# python3
# Given a pattern and a string str, find if str follows the same pattern.

# Here follow means a full match, such that there is a bijection
# between a letter in pattern and a non-empty word in str.

# Examples:
# pattern = "abba", str = "dog cat cat dog" should return true.
# pattern = "abba", str = "dog cat cat fish" should return false.
# pattern = "aaaa", str = "dog cat cat dog" should return false.
# pattern = "abba", str = "dog dog dog dog" should return false.
# Notes:
# ou may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.


# My solution
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        dict_pattern_to_str = {}
        dict_str_to_pattern = {}
        str_list = str.split()
        if len(str_list) != len(pattern):
            return False
        for i in range(len(pattern)):
            if str_list[i] not in dict_str_to_pattern and pattern[i] not in dict_pattern_to_str:
                dict_str_to_pattern[str_list[i]] = pattern[i]
                dict_pattern_to_str[pattern[i]] = str_list[i]
            elif str_list[i] in dict_str_to_pattern and pattern[i] in dict_pattern_to_str:
                if dict_str_to_pattern[str_list[i]] != pattern[i] or dict_pattern_to_str[pattern[i]] != str_list[i]:
                    return False
            else:
                return False
        return True
