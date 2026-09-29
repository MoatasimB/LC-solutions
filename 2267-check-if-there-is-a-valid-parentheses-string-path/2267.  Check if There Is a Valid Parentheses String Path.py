class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        
        m = len(grid)
        n = len(grid[0])
        def valid(r, c):
            return 0 <= r < m and 0 <= c < n
        
        memo = {}
        def dfs(r, c, count):
            if (r, c, count) in memo:
                return memo[(r, c, count)]
            if count < 0:
                return False
            if (r, c) == (m - 1, n - 1):
                return count == 0

            dr, dc = r + 1, c
            rr, rc = r, c + 1

            if valid(dr, dc):
                if grid[dr][dc] == "(":
                    if dfs(dr, dc, count + 1):
                        return True
                else:
                    if dfs(dr, dc, count - 1):
                        return True
            
            if valid(rr, rc):
                if grid[rr][rc] == "(":
                    if dfs(rr, rc, count + 1):
                        return True
                else:
                    if dfs(rr, rc, count - 1):
                        return True
            memo[(r, c, count)] = False
            return False
        
        count = 0
        if grid[0][0] == "(":
            count += 1
        else:
            count -= 1
        return dfs(0, 0, count)
                    

