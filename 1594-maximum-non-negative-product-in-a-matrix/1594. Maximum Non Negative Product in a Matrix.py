class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

                
        memo = {}
        def dfs(r, c):
            if (r, c) in memo:
                return memo[(r, c)]
            if r == 0 and c == 0:
                return [grid[r][c], grid[r][c]]
            if r < 0 or c < 0:
                return [float("inf"), float("-inf")]

            upMin, upMax = dfs(r, c - 1)
            leftMin, leftMax = dfs(r - 1, c)

            newMin = min(upMin, leftMin)
            newMax = max(upMax, leftMax)

            ans = [min(grid[r][c] * newMax, grid[r][c] * newMin), max(grid[r][c] * newMax, grid[r][c] * newMin)]

            memo[(r, c)] = ans
            # #maxNegProd
            # newMin = min(grid[r][c] * upMin, grid[r][c] * leftMin)

            # #maxPosProd
            # newMax = max(grid[r][c] * upMax, grid[r][c] * leftMax)

            return ans
        
        final = max(dfs(m - 1, n - 1))

        return final % (10**9 + 7) if final >= 0 else -1
        
