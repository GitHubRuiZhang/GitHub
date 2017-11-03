# python3
# Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's,
# empty slots are represented with '.'s. You may assume the following rules:

# You receive a valid board, made of only battleships or empty slots.
# Battleships can only be placed horizontally or vertically.
# In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column),
# where N can be of any size.
# At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.
# Example:
# X..X
# ...X
# ...X
# In the above board there are 2 battleships.
# Invalid Example:
# ...X
# XXXX
# ...X
# This is an invalid board that you will not receive - as battleships will always have a cell separating between them.
# Follow up:
# Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?


# My solution
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count = 0
        visited = [[False for i in range(len(board[0]))] for j in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if visited[i][j] == False:
                    if board[i][j] == 'X':
                        j_in = j + 1
                        i_in = i + 1
                        if j_in < len(board[0]) and i_in < len(board) and board[i_in][j] == 'X' and board[i][
                            j_in] == 'X':
                            return False
                        while j_in < len(board[0]) and board[i][j_in] == 'X':
                            if visited[i][j_in] == True:
                                return False
                            visited[i][j_in] = True
                            j_in += 1
                        while i_in < len(board) and board[i_in][j] == 'X':
                            if visited[i_in][j] == True:
                                return False
                            visited[i_in][j] = True
                            i_in += 1
                        count += 1
                    visited[i][j] == True

        return count


# Solution with a lower memory requirement
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X' and (board[i][j - 1] == '.' or j == 0) and (board[i - 1][j] == '.' or i == 0):
                    count += 1

        return count
