class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ans = 0
        def dfs(i,j):
            if i < 0 or j <0:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            dp[(i,j)] = 0
            curr = min(dfs(i-1,j),dfs(i, j-1), dfs(i-1,j-1))

            if matrix[i][j] == "1":
                dp[(i,j)] = curr + 1
            return dp[(i,j)]
            
            
      

        dp = {}
        dfs(len(matrix)-1, len(matrix[0])-1)
        return max(dp.values())**2 if dp.values() else 0