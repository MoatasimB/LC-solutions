class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        m = len(matrix)
        n = len(matrix[0])
        
        def valid(r,c):
            return 0<=r<m and 0<=c<n
        
        lgt_p = defaultdict(int) #(r,c) : longest inc from this node
        
        def bfs(r, c):
            ogr = r
            ogc = c
            q = deque()
            q.append((r,c, 1))
            seen = set()
            seen.add((r,c))
            ans = 0
            while q:
                r,c, p_len = q.popleft()
                ans = max(ans, p_len)
                for dx, dy in dirs:
                    nr, nc = r + dx, c + dy
                    if valid(nr,nc) and matrix[nr][nc] > matrix[r][c] and (nr,nc) not in seen:
                        seen.add((nr,nc))
                        if (nr,nc) not in lgt_p:
                            bfs(nr,nc)
 
                        ans = max(ans, p_len + lgt_p[(nr,nc)])
                            
            
            lgt_p[(ogr,ogc)] = ans
        
        for r in range(m):
            for c in range(n):
                bfs(r,c)
                
        
        return max(lgt_p.values())
                    
                
        [[7,6,1,1],
         [2,7,6,0],
         [1,3,5,1],
         [6,6,3,2]]
                            
            
            