class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = {}
        def dfs(i,j):
            if obstacleGrid[i][j] == 1:
                return 0
            if i==0 and j == 0:
                return 1
            if i < 0 or j < 0:
                return 0

            
            if (i,j) in dp:
                return dp[(i,j)]
            
            up = dfs(i-1, j)
            left = dfs(i, j-1)
            dp[(i,j)] = up + left
            return dp[(i,j)]
        
        return dfs(len(obstacleGrid)-1, len(obstacleGrid[0]) - 1)