class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m = len(board)
        n = len(board[0])
        
        def valid(r,c):
            return 0<=r<m and 0<=c<n
        
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]

        def dfs(r, c, i, seen):
            if i == len(word):
                return True
            for dx, dy in dirs:
                nr = dx + r
                nc = dy + c
                if valid(nr,nc) and (nr,nc) not in seen and board[nr][nc] == word[i]:
                    seen.add((nr,nc))
                    if dfs(nr,nc,i+1, seen):
                        return True
                    
                    seen.remove((nr,nc))
        

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i,j,1, set([(i,j)])):
                        return True
        
        return False

