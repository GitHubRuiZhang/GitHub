# python3
# Write a program to solve a Sudoku puzzle by filling the empty cells.

# Empty cells are indicated by the character '.'.

# You may assume that there will be only one unique solution.


# My solution
class Solution(object):
    def global_board(self, board):
        self.board = board

    def find(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == '.':
                    return i, j
        return -1, -1

    def search(self):
        i, j = self.find()
        if i == -1 and j == -1:
            return True

        for it in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if self.verify(i, j, it):
                self.board[i][j] = it
                if self.search():
                    return True
                self.board[i][j] = '.'
        return False

    def verify(self, r, c, num):
        for i in range(9):
            if self.board[r][i] == num:
                return False
        for j in range(9):
            if self.board[j][c] == num:
                return False
        resr = r // 3
        resc = c // 3
        for i in range(3):
            for j in range(3):
                if self.board[3 * resr + i][3 * resc + j] == num:
                    return False
        return True

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.global_board(board)
        self.search()
