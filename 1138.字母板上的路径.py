#
# @lc app=leetcode.cn id=1238 lang=python3
#
# [1138] 字母板上的路径
#

# @lc code=start
def get_pos(start=[0, 0], end='z'):
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z****"]
        if board[start[0]][start[1]] == end:
            return '', start
        flag = [[0, 0, 0, 0, 0] for i in range(6)]
        flag[-1] = [0, 1, 1, 1, 1]
        nodes = [('', start)]
        while nodes:
            tmp = []
            for i, node in enumerate(nodes):
                p = node[0]
                row, col = node[1]
                if col > 0 and flag[row][col-1] == 0:
                    if board[row][col-1] == end:
                        return p+"L", [row, col-1]
                    else:
                        tmp.append((p+"L", [row, col-1]))
                        flag[row][col-1] = 1
                if row > 0 and flag[row-1][col] == 0:
                    if board[row-1][col] == end:
                        return p+"U", [row-1, col]
                    else:
                        tmp.append((p+"U", [row-1, col]))
                        flag[row-1][col] = 1
                if col < len(board[row]) - 1 and flag[row][col+1] == 0:
                    if board[row][col+1] == end:
                        return p+"R", [row, col+1]
                    else:
                        tmp.append((p+"R", [row, col+1]))
                        flag[row][col+1] = 1
                #print(row, col)
                if row < 5 and flag[row+1][col] == 0:
                    if board[row+1][col] == end:
                        return p+"D", [row+1, col]
                    else:
                        tmp.append((p+"D", [row+1, col]))
                        flag[row+1][col] = 1
            if i == len(nodes) - 1:
                nodes = tmp
class Solution:
    
    def alphabetBoardPath(self, target: str) -> str:
        res = ''
        start = [0, 0]
        for i in range(len(target)):
            path, pos = get_pos(start, target[i])
            start = pos
            res = res + path + "!"
        return res
# @lc code=end

