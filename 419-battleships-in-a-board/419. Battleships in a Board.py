class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        
        m = len(board)
        n = len(board[0])
        def valid(r,c):
            return 0<=r<m and 0<=c<n and board[r][c] == "X"

        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        seen = [[False] * n for _ in range(m)]
        def dfs(r,c):
            seen[r][c] = True
            for dx, dy in dirs:
                nr = r + dx
                nc = c + dy
                if valid(nr, nc) and not seen[nr][nc]:
                    dfs(nr, nc)
        
        count = 0
        for r in range(m):
            for c in range(n):
                if board[r][c] == "X" and not seen[r][c]:
                    dfs(r,c)
                    count += 1
        
        return count