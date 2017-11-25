# python3
# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

# Note:
# A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.


# My solution
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if len(board) % 3 != 0 and len(board[0]) % 3 != 0:
            return False

        for i in range(len(board)):
            r = []
            c = []
            for j in range(len(board)):
                if board[i][j] != '.' and board[i][j] in r:
                    return False
                elif board[i][j] != '.':
                    r.append(board[i][j])

                if board[j][i] != '.' and board[j][i] in c:
                    return False
                elif board[j][i] != '.':
                    c.append(board[j][i])

        num = len(board) // 3
        for i in range(num):
            for j in range(num):
                count = []
                for m in range(3):
                    for n in range(3):
                        if board[i * 3 + m][j * 3 + n] != '.' and board[i * 3 + m][j * 3 + n] in count:
                            return False
                        elif board[i * 3 + m][j * 3 + n] != '.':
                            count.append(board[i * 3 + m][j * 3 + n])

        return True








