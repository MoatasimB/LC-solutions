class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        
        def check():
            for r in range(3):
                for c in range(3):
                    if grid[r][c] != 1:
                        return False
            return True

        final = float("inf")
        def dfs(moves):
            nonlocal final
            if check():
                final = min(final, moves)
                return
            
            for r in range(3):
                for c in range(3):
                    if grid[r][c] > 1:


                        for x in range(3):
                            for y in range(3):
                                if grid[x][y] == 0:
                                    grid[x][y] = 1
                                    grid[r][c] -= 1

                                    dfs(moves + abs(r - x) + abs(c - y))
                                    grid[x][y] = 0
                                    grid[r][c] += 1
        
        dfs(0)
        return final