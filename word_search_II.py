# python3
# Given a 2D board and a list of words from the dictionary, find all words in the board.

# Each word must be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring.
# The same letter cell may not be used more than once in a word.

# For example,
# Given words = ["oath","pea","eat","rain"] and board =

# [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# Return ["eat","oath"].
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.


# My solution
class PreNode(object):
    def __init__(self, val):
        self.val = val
        self.next = []


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = PreNode(None)

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        word += '$'
        for i in range(len(word)):
            inside = False
            for it in node.next:
                if it.val == word[i]:
                    inside = True
                    node = it
                    break
            if not inside:
                break
        while i < len(word):
            res = PreNode(word[i])
            node.next.append(res)
            node = res
            i += 1

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        word += '$'
        res = self.root.next
        for i in range(len(word)):
            inside = False
            for it in res:
                if it.val == word[i]:
                    inside = True
                    res = it.next
                    break
            if not inside:
                break
        if inside == False:
            return False
        else:
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
                break
        if inside == False:
            return False
        else:
            return True


class Solution(object):
    def __init__(self):
        self.out = set()

    def dfs(self, root, i, j, board, path):
        for it in root.next:
            if it.val == '$':
                self.out.add(path)

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        res = board[i][j]
        node = None
        for it in root.next:
            if it.val == res:
                node = it
                break
        if node == None:
            return
        board[i][j] = '#'
        self.dfs(node, i + 1, j, board, path + res)
        self.dfs(node, i - 1, j, board, path + res)
        self.dfs(node, i, j + 1, board, path + res)
        self.dfs(node, i, j - 1, board, path + res)
        board[i][j] = res
        return

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = Trie()
        words = set(words)
        for word in words:
            trie.insert(word)

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(trie.root, i, j, board, "")

        return list(self.out)
