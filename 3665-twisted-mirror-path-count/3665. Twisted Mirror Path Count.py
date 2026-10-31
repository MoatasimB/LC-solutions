class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        MOD = 10**9 + 7
        memo = {}
        def dfs(r, c, prev):
            if (r, c, prev) in memo:
                return memo[(r, c, prev)]
            if (r, c) == (m - 1, n - 1):
                return 1
            if r > m - 1 or c > n - 1:
                return 0
            
            count = 0
            if grid[r][c] == 1:
                if prev == "R":
                    count += dfs(r + 1, c, "D") % MOD
                else:
                    count += dfs(r, c + 1, "R") % MOD
            else:
                #go down
                count += dfs(r + 1, c, "D") % MOD

                #go right
                count += dfs(r, c + 1, "R") % MOD
            memo[(r, c, prev)] = count % MOD
            return count
        return dfs(0, 0, "X") % MOD
