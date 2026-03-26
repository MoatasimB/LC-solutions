class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        
        m = len(grid)
        n = len(grid[0])

        horizontal = [[0] * n for _ in range(m)]
        vertical = [[0] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                horizontal[r][c] = grid[r][c] + (horizontal[r][c - 1] if c - 1 >= 0 else 0)
                vertical[r][c] = grid[r][c] + (vertical[r - 1][c] if r - 1 >= 0 else 0)
        
        finalHorizontal = []
        finalVertical = []
        curr = 0
        for r in range(m):
            curr += horizontal[r][n - 1]
            finalHorizontal.append(curr)
        
        curr = 0
        for c in range(n):
            curr += vertical[m - 1][c]
            finalVertical.append(curr)

        for i in range(len(finalHorizontal)):
            top = finalHorizontal[i]
            bottom = finalHorizontal[-1] - top
            if top == bottom:
                return True
        
        for i in range(len(finalVertical)):
            left = finalVertical[i]
            right = finalVertical[-1] - left
            if left == right:
                return True
    
        return False