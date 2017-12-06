# python3
# Implement a trie with insert, search, and startsWith methods.

# Note:
# You may assume that all inputs are consist of lowercase letters a-z.


# My solution
class Node(object):
    def __init__(self, value):
        self.val = value
        self.next = []


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node(None)

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        word += '$'
        node = self.root
        for i in range(len(word)):
            inside = False
            for it in node.next:
                if it.val == word[i]:
                    inside = True
                    node = it
                    break
            if not inside:
                res = Node(word[i])
                node.next.append(res)
                node = res

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        word += '$'
        node = self.root
        for i in range(len(word)):
            inside = False
            for it in node.next:
                if it.val == word[i]:
                    inside = True
                    node = it
                    break
            if not inside:
                return False
        return True

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for i in range(len(prefix)):
            inside = False
            for it in node.next:
                if it.val == prefix[i]:
                    inside = True
                    node = it
                    break
            if not inside:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)