class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        pos = [-1] * n

        for r in range(n):
            for c in range(n - 1, -1, -1):
                if grid[r][c] == 1:
                    pos[r] = c
                    break

        # 2
        # 1
        # 0

        

        ans = 0        
        for r in range(n):
            found = -1
            for row in range(r, n):
                print(row, n - pos[row] - 1, n - r - 1)
                if n - pos[row] - 1 >= n - r - 1:
                    found = row
                    break
            if found == -1:
                return -1
            else:
                ans += found - r
                for j in range(found, r, -1):
                    pos[j], pos[j - 1] = pos[j - 1], pos[j]
        
        return ans
        

                