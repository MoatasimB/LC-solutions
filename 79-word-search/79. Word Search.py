class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m = len(board)
        n = len(board[0])

        def valid(r,c):
            return 0<=r<m and 0<=c<n
        
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]

        def dfs(r,c,i, curr, seen):
            # print(seen)
            if "".join(curr) == word:
                return True
            
            for dx, dy in dirs:
                nr,nc = r + dx, c + dy

                if valid(nr,nc) and (nr, nc) not in seen and board[nr][nc] == word[i]:
                    seen.add((nr,nc))
                    curr.append(board[nr][nc])
                    if dfs(nr,nc,i+1,curr,seen):
                        return True
                    
                    seen.remove((nr,nc))
                    curr.pop()
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i,j,1,[board[i][j]], set([(i,j)])):
                    return True
        
        return False
                    


