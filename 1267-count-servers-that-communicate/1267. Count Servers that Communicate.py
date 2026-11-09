class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        rows = defaultdict(int)
        cols = defaultdict(int)
        comps = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1
                    comps.append((i, j))
        
        ans = 0
        for x, y in comps:
            if rows[x] > 1 or cols[y] > 1:
                ans += 1
        
        return ans
        
