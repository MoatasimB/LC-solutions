class Solution:
    def isThereAPath(self, grid: List[List[int]]) -> bool:
        
        dp = {}
        def dfs(i,j,ones,zeros):
            if (i,j,ones,zeros) in dp:
                return dp[(i,j,ones,zeros)]
            if i==0 and j==0:
                if grid[i][j] == 0 and 1 + zeros == ones:
                    return True
                elif grid[i][j] == 1 and 1 + ones == zeros:
                    return True
                else:
                    return False
            if i < 0 or j < 0:
                return False

            curr = grid[i][j]

            if curr == 1:
                left = dfs(i, j-1, ones + 1, zeros)
                up = dfs(i-1, j, ones+1, zeros)
                
                dp[(i,j,ones,zeros)] = left or up
                return left or up
            if curr == 0:
                left = dfs(i, j-1, ones, zeros + 1)
                up = dfs(i-1, j, ones, zeros + 1)
                
                dp[(i,j,ones,zeros)] = left or up
                return left or up
        
        return dfs(len(grid)-1, len(grid[0]) - 1, 0, 0)

