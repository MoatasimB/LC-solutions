class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        
        m = len(boxGrid)
        n = len(boxGrid[0])

        grid = [["."] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                grid[j][m - i - 1] = boxGrid[i][j]

        # print(grid)
        for col in range(m):
            idx = n
            for row in range(n - 1, -1, -1):
                if grid[row][col] == "#":
                    grid[row][col] = "."
                    grid[idx - 1][col] = "#"
                    idx -= 1
                elif grid[row][col] == "*":
                    idx = row
        
        return grid