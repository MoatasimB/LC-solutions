class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def valid(r, c):
            return 0 <= r < m and 0 <= c < n
        
        dirs = [(0, 1), (1,0), (0, -1), (-1,0)]


        def dfs(i, r, c, seen):
            if i == len(word):
                return True
            
            for dx, dy in dirs:
                nr = r + dx
                nc = c + dy

                if valid(nr, nc) and (nr, nc) not in seen and board[nr][nc] == word[i]:
                    seen.add((nr, nc))
                    if dfs(i + 1, nr, nc, seen):
                        return True
                    seen.remove((nr,nc))
            
            return False
        

        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    if dfs(1, r, c, set([(r, c)])):
                        return True
        
        return False
