#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
class Solution:
    def __init__(self):
        self.res = []
    def is_valid(self, board, row, col):
        if 'Q' in board[row]:
            return False
        # top
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        for i in range(1, row+1):
            # left top
            if row-i >= 0 and col - i >=0 and board[row-i][col-i]  == 'Q':
                return False
            # right top
            if row-i >= 0 and col + i < len(board) and board[row-i][col+i]  == 'Q':
                return False
        return True
    def backtrack(self, board, row):
        if row == len(board):
            tmp = [''.join(board[i]) for i in range(len(board))]
            self.res.append(tmp)
            return
        for col in range(len(board[row])):
            if not self.is_valid(board, row, col):
                continue
            board[row][col] = 'Q'
            self.backtrack(board, row + 1)
            board[row][col] = '.'
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for i in range(n)]
        self.backtrack(board, 0)
        return self.res
# @lc code=end

