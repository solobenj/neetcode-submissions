class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        grid = [0] * 9
        for y, r in enumerate(board):
            for x, c in enumerate(r):
                if c == ".": continue

                val = int(board[y][x]) - 1
                mask = 1 << val

                if mask & rows[y]: return False
                if mask & cols[x]: return False
                key = (y//3)*3 + (x//3)
                if mask & grid[key]: return False

                rows[y] |= mask
                cols[x] |= mask
                grid[key] |= mask

        return True