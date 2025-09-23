class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
                
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        m = len(matrix)
        n = len(matrix[0])
        
        def valid(r,c):
            return 0<=r<m and 0<=c<n
        
        lip = {}
        
        def dfs(r,c):
            if (r,c) in lip:
                return lip[(r,c)]
            ans = 1
            for dx, dy in dirs:
                nr, nc = dx + r, dy + c

                if valid(nr,nc) and matrix[nr][nc] > matrix[r][c]:
                    ans = max(ans, 1 + dfs(nr,nc))
            
            lip[(r,c)] = ans
            return ans
        
        for r in range(m):
            for c in range(n):
                dfs(r,c)
        
        return max(lip.values())