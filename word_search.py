# python3
# Given a 2D board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring.
# The same letter cell may not be used more than once.

# For example,
# Given board =

# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.


# My solution
class Solution(object):
    def dfs(self, word, i, j, board, visited):
        if word == '':
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j] == True or word[0] != board[i][j]:
            return False
        visited[i][j] = True
        res = word[1:]
        if self.dfs(res, i + 1, j, board, visited) or self.dfs(res, i - 1, j, board, visited) or self.dfs(res, i, j + 1,
                                                                                                          board,
                                                                                                          visited) or self.dfs(
                res, i, j - 1, board, visited):
            return True
        visited[i][j] = False
        return False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # fast
        visited = [[False for j in range(len(board[0]))] for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(word, i, j, board, visited):
                    return True

        return False

        # slow
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        letters = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in letters:
                    letters[board[i][j]].add((i, j))
                else:
                    letters[board[i][j]] = set([(i, j)])

        def search(word, i, pos, letters, visited):
            if i == len(word):
                return True
            cur = word[i]
            if cur not in letters:
                return False
            all_possible = [(pos[0] + it[0], pos[1] + it[1]) for it in directions]
            out = False
            for it in letters[cur]:
                if it in all_possible and visited[it[0]][it[1]] == False:
                    visited[it[0]][it[1]] = True
                    if search(word, i + 1, it, letters, visited):
                        return True
                    visited[it[0]][it[1]] = False

            return False

        visited = [[False for j in range(len(board[0]))] for i in range(len(board))]
        cur = word[0]
        if cur not in letters:
            return False
        for it in letters[cur]:
            visited[it[0]][it[1]] = True
            if search(word, 1, it, letters, visited):
                return True
            visited[it[0]][it[1]] = False
        return False







