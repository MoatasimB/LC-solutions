class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        negDiag = set()
        posDiag = set()
        col = set()
        ans = []
        board = [["."] * n for _ in range(n)]
        def dfs(r):
            if r == n:
                ans.append(["".join(row) for row in board[:]])
                return
            
            for c in range(n):
                if c not in col and r + c not in posDiag and r - c not in negDiag:
                    col.add(c)
                    posDiag.add(r + c)
                    negDiag.add(r - c)

                    board[r][c] = "Q"

                    dfs(r + 1)

                    col.remove(c)
                    posDiag.remove(r + c)
                    negDiag.remove(r - c)

                    board[r][c] = "."
        
        dfs(0)
        return ans


