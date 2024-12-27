class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row = set()
        col = set()
        box = set()

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue
                if (r,board[r][c]) in row:
                    print(1)
                    print(r,board[r][c])
                    return False
                if (c,board[r][c]) in col:
                    print(2)
                    return False
                if (r//3, c//3,board[r][c]) in box:
                    print(3)
                    return False
                row.add((r,board[r][c]))
                col.add((c,board[r][c]))
                box.add((r//3, c//3,board[r][c]))
    
        return True