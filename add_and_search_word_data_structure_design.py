# python3
# Design a data structure that supports the following two operations:

# void addWord(word)
# bool search(word)
# search(word) can search a literal word or a regular expression string containing only letters a-z or .. A .
#  means it can represent any one letter.

# For example:

# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
# Note:
# You may assume that all words are consist of lowercase letters a-z.


# My solution
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        if len(word) in self.words:
            self.words[len(word)].append(word)
        else:
            self.words[len(word)] = [word]

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        n = len(word)
        if n not in self.words:
            return False
        for it in self.words[n]:
            find = True
            for i in range(n):
                if word[i] != '.' and word[i] != it[i]:
                    find = False
                    break
            if find:
                return True
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)