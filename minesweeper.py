# python3
# Let's play the minesweeper game (Wikipedia, online game)!

# You are given a 2D char matrix representing the game board.
# 'M' represents an unrevealed mine,
# 'E' represents an unrevealed empty square,
# 'B' represents a revealed blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines,
# digit ('1' to '8') represents how many mines are adjacent to this revealed square,
# and finally 'X' represents a revealed mine.

# Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'),
# return the board after revealing this position according to the following rules:

# If a mine ('M') is revealed, then the game is over - change it to 'X'.
# If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B')
# and all of its adjacent unrevealed squares should be revealed recursively.
# If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8')
# representing the number of adjacent mines.
# Return the board when no more squares will be revealed.
# Example 1:
# Input:

# [['E', 'E', 'E', 'E', 'E'],
#  ['E', 'E', 'M', 'E', 'E'],
#  ['E', 'E', 'E', 'E', 'E'],
#  ['E', 'E', 'E', 'E', 'E']]

# Click : [3,0]

# Output:

# [['B', '1', 'E', '1', 'B'],
#  ['B', '1', 'M', '1', 'B'],
#  ['B', '1', '1', '1', 'B'],
#  ['B', 'B', 'B', 'B', 'B']]

# Explanation:

# Example 2:
# Input:

# [['B', '1', 'E', '1', 'B'],
#  ['B', '1', 'M', '1', 'B'],
#  ['B', '1', '1', '1', 'B'],
#  ['B', 'B', 'B', 'B', 'B']]

# Click : [1,2]

# Output:

# [['B', '1', 'E', '1', 'B'],
#  ['B', '1', 'X', '1', 'B'],
#  ['B', '1', '1', '1', 'B'],
#  ['B', 'B', 'B', 'B', 'B']]

# Explanation:

# Note:
# The range of the input matrix's height and width is [1,50].
# The click position will only be an unrevealed square ('M' or 'E'), which also means the input board contains
# at least one clickable square.
# The input board won't be a stage when game is over (some mines have been revealed).
# For simplicity, not mentioned rules should be ignored in this problem. For example,
# you don't need to reveal all the unrevealed mines when the game is over,
# consider any cases that you will win the game or flag any squares.


# My solution
class Solution(object):
    def findMine(self, board, click):
        count = 0
        for i in range(3):
            current_x = click[0] - 1 + i
            if 0 <= current_x < len(board):
                for j in range(3):
                    current_y = click[1] - 1 + j
                    if 0 <= current_y < len(board[0]):
                        if board[current_x][current_y] in 'MX':
                            count += 1

        return count

    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if board[click[0]][click[1]] == 'M' or board[click[0]][click[1]] == 'MB':
            board[click[0]][click[1]] = 'X'
            return board
        count = self.findMine(board, click)
        if count > 0:
            board[click[0]][click[1]] = str(count)
            return board
        board[click[0]][click[1]] = 'B'
        new_clicks = [tuple(click)]
        while new_clicks:
            click = new_clicks.pop()
            for i in range(3):
                current_x = click[0] + 1 - i
                if 0 <= current_x < len(board):
                    for j in range(3):
                        current_y = click[1] + 1 - j
                        if 0 <= current_y < len(board[0]):
                            if board[current_x][current_y] == 'E':
                                count = self.findMine(board, [current_x, current_y])
                                if count == 0:
                                    board[current_x][current_y] = 'B'
                                    new_clicks.append(tuple([current_x, current_y]))
                                else:
                                    board[current_x][current_y] = str(count)

        return board
