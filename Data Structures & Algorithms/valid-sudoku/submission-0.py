class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            rset = set()
            for c in row:
                if c == ".":
                    continue
                if c in rset:
                    return False
                rset.add(c)
        for column_i in range(9):
            cset = set()
            for r in board:
                if r[column_i] == ".":
                    continue
                if r[column_i] in cset:
                    return False
                cset.add(r[column_i])
        for s in range(9):
            sset = set()
            for r in range(3):
                for c in range(3):
                    row = (s//3) * 3 + r
                    col = (s % 3) * 3 + c
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in sset:
                        return False
                    sset.add(board[row][col])
        return True
