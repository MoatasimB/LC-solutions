class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        
        # [
        #     [6,7,1,20,11],
        #     [4,5,18,23,28]
        #     ]
        
        m = len(grid)
        n = len(grid[0])
        points = [(i, j) for i in range(m) for j in range(n)]
        points.sort(key=lambda x:grid[x[0]][x[1]])
        dp = [[float("inf")] * n for _ in range(m)]
        
        for t in range(k + 1):
            preMin = float("inf")
            j = 0
            for p in range(len(points)):
                preMin = min(preMin, dp[points[p][0]][points[p][1]])

                if p + 1 < len(points) and grid[points[p][0]][points[p][1]] == grid[points[p + 1][0]][points[p + 1][1]]:
                    continue
                for k in range(j, p + 1):
                    dp[points[k][0]][points[k][1]] = min(dp[points[k][0]][points[k][1]], preMin)
                

                j = p + 1
            
            for k in range(j, len(points)):
                    dp[points[k][0]][points[k][1]] = min(dp[points[k][0]][points[k][1]], preMin)
            

            for i in range(m - 1, -1, -1):
                for j in range(n - 1, -1, -1):
                    if (i, j) == (m - 1, n - 1):
                        dp[i][j] = 0
                        continue
                    down = dp[i + 1][j] + grid[i + 1][j] if i + 1 < m else float("inf")
                    right = dp[i][j + 1] + grid[i][j + 1] if j + 1 < n else float("inf")
                    dp[i][j] = min(dp[i][j], down, right)
        return dp[0][0]
        

[[1,3,3],
[2,5,4],
[4,3,5]]