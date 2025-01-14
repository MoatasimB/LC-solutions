class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # dp = {}
        # def dfs(i,j):
        #     if obstacleGrid[i][j] == 1:
        #         return 0
        #     if i==0 and j == 0:
        #         return 1
        #     if i < 0 or j < 0:
        #         return 0

            
        #     if (i,j) in dp:
        #         return dp[(i,j)]
            
        #     up = dfs(i-1, j)
        #     left = dfs(i, j-1)
        #     dp[(i,j)] = up + left
        #     return dp[(i,j)]
        
        # return dfs(len(obstacleGrid)-1, len(obstacleGrid[0]) - 1)
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        # dp = [[0]*n for _ in range(m)]
        
        
        prev = [0] * n
        prev[0] = 1 if obstacleGrid[0][0] != 1 else 0
        
        for i in range(1,n):
            if obstacleGrid[0][i] == 1:
                continue
            prev[i] = prev[i-1]
        
        for i in range(1,m):
            curr = [0] * n
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    continue

         
                up = prev[j]
                left = 0
                if j > 0:
                    left = curr[j-1]
                
                curr[j] = up + left
            prev = curr
        return prev[n-1]