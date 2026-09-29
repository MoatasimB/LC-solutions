class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        
        m = len(grid)
        n = len(grid[0])
        def valid(r, c):
            return 0 <= r < m and 0 <= c < n
        
        memo = {}
        def dfs(r, c, left, right):
            if (r, c, left, right) in memo:
                return memo[(r, c, left, right)]
            if right > left:
                return False
            if (r, c) == (m - 1, n - 1):
                return left == right

            dr, dc = r + 1, c
            rr, rc = r, c + 1

            if valid(dr, dc):
                if grid[dr][dc] == "(":
                    if dfs(dr, dc, left + 1, right):
                        return True
                else:
                    if dfs(dr, dc, left, right + 1):
                        return True
            
            if valid(rr, rc):
                if grid[rr][rc] == "(":
                    if dfs(rr, rc, left + 1, right):
                        return True
                else:
                    if dfs(rr, rc, left, right + 1):
                        return True
            memo[(r, c, left, right)] = False
            return False
        
        left_count = 0
        right_count = 0
        if grid[0][0] == "(":
            left_count += 1
        else:
            right_count += 1
        return dfs(0, 0, left_count, right_count)
                    

