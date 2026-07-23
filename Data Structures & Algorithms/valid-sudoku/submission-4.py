class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            rows = set()
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows:
                    return False
                rows.add(board[r][c])

        for c in range(9):
            cols = set()
            for r in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in cols:
                    return False
                cols.add(board[r][c])

        for square in range(9):
            seen = set()
            for r in range(3):
                for c in range(3):
                    row = (square // 3) * 3 + r
                    col = (square % 3) * 3 + c
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True
