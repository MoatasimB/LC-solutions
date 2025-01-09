class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = {}
        def dfs(i,j):
            if i == n - 1:
                return triangle[i][j]
            if (i,j) in dp:
                return dp[(i,j)]
            
            down = dfs(i+1, j)
            diagonal = dfs(i+1, j+1)
            print(down, diagonal)
            dp[(i,j)] = triangle[i][j] + min(down, diagonal)
            
            return dp[(i,j)]
        
        return dfs(0,0)