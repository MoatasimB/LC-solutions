class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # dp = {}
        # def dfs(i,j):
        #     if (i,j) in dp:
        #         return dp[(i,j)]
        #     if i==0 and j==0:
        #         return grid[i][j]
        #     if i < 0 or j < 0:
        #         return float('inf')
            
        #     left = grid[i][j] + dfs(i, j-1)
        #     up = grid[i][j] + dfs(i-1, j)

        #     dp[(i,j)] = min(left, up)
        #     return dp[(i,j)]
        
        # return dfs(len(grid) - 1, len(grid[0]) - 1)

        dp = [[float('inf')] * len(grid[0]) for _ in range(len(grid))]
        dp[0][0] = grid[0][0]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                left = float('inf')
                up = float('inf')
                if j > 0:
                    left = dp[i][j-1]
                if i > 0:
                    up = dp[i-1][j]
                dp[i][j] = grid[i][j] + min(up, left)
        print(dp)
        return dp[len(grid) - 1][len(grid[0])-1]