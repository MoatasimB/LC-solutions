class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != ".":
                    rows[r].add(int(val))
                    cols[c].add(int(val))
                    boxes[(r // 3, c // 3)].add(int(val))
        
        def dfs(r, c, board):
            if r == 9 and c == 9:
                return True
            val = board[r][c]
            if val != ".":
                nr = r + 1 if c == 8 else r
                nc = c + 1
                if nr != 9 and nc == 9:
                    nc = 0
                
                if dfs(nr, nc, board):
                    return True
            else:
                for num in range(1, 10):
                    if num not in rows[r] and num not in cols[c] and num not in boxes[(r//3, c//3)]:
                        rows[r].add(num)
                        cols[c].add(num)
                        boxes[(r // 3, c // 3)].add(num)

                        board[r][c] = str(num)
                        nr = r + 1 if c == 8 else r
                        nc = c + 1
                        if nr != 9 and nc == 9:
                            nc = 0
                        
                        if dfs(nr, nc, board):
                            return True
                        rows[r].remove(num)
                        cols[c].remove(num)
                        boxes[(r // 3, c // 3)].remove(num)
                        board[r][c] = "."

                return False
        
        dfs(0, 0, board)
        return board

