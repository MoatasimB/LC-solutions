class Solution:
    def minimumOR(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        ans = 0
        
        for r in range(m):
            for c in range(n):
                ans |= grid[r][c]

        for i in reversed(range(32)):
            if not (ans & ( 1 << i)):
                continue

            
            curr = ans ^ (1 << i)
            valid = True
            for r in range(m):
                if not any(a & ~curr == 0 for a in grid[r]):
                    valid = False

            if valid:
                ans = curr

        return ans

        heap = []
        seen = set()

        for c in range(n):
            heapq.heappush(heap, [grid[0][c], 1])
        
        while heap:
            val, row = heapq.heappop(heap)

            if row == m:
                return val
            if (val, row) in seen:
                continue
            seen.add((val,row))
            for c in range(n):
                heapq.heappush(heap, [val | grid[row][c], row + 1])
            
        
        # 001 101
        # 010 100

        # # 011  101
        # # 110  100

        # 110001.  001010
        # 010110.  111111
        
        # memo = {}
        
        # def dfs(r, curr):
        #     if (r, curr) in memo:
        #         return memo[(r, curr)]
        #     if r == m:
        #         return curr
        #     ans = float("inf")
        #     for c in range(n):
        #         ans = min(ans, dfs(r + 1, curr | grid[r][c]))
        #     memo[(r, curr)] = ans
        #     return ans

        # return dfs(0, 0)