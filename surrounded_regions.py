# python3
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.

# For example,
# X X X X
# X O O X
# X  X O X
# X O X X
# After running your function, the board should be:

# X X X X
# X X X X
# X X X X
# X O X X


# My solution
import Queue


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board == [] or board == [[]]:
            return
        all_points = Queue.Queue()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i == 0 or j == 0 or i == len(board) - 1 or j == len(board[0]) - 1):
                    board[i][j] = 'S'
                    all_points.put((i, j))

        Test = all_points.empty()
        while (not Test):
            cur = all_points.get()
            if cur[0] > 0 and board[cur[0] - 1][cur[1]] == 'O':
                board[cur[0] - 1][cur[1]] = 'S'
                all_points.put((cur[0] - 1, cur[1]))
            if cur[0] < len(board) - 1 and board[cur[0] + 1][cur[1]] == 'O':
                board[cur[0] + 1][cur[1]] = 'S'
                all_points.put((cur[0] + 1, cur[1]))
            if cur[1] > 0 and board[cur[0]][cur[1] - 1] == 'O':
                board[cur[0]][cur[1] - 1] = 'S'
                all_points.put((cur[0], cur[1] - 1))
            if cur[1] < len(board[0]) - 1 and board[cur[0]][cur[1] + 1] == 'O':
                board[cur[0]][cur[1] + 1] = 'S'
                all_points.put((cur[0], cur[1] + 1))
            Test = all_points.empty()

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'S':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

        return

