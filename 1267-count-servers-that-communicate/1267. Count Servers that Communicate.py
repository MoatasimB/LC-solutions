class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        comps = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    rows[i].add((i,j))
                    cols[j].add((i,j))
                    comps.append((i, j))
        
        ans = 0
        for x, y in comps:
            if len(rows[x]) > 1 or len(cols[y]) > 1:
                ans += 1
        
        return ans
        
