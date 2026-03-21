class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        

        m = len(grid)
        n = len(grid[0])

        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]

        [
            [1,8],
            [3,-2]
        
        ]

        for r in range(m - k + 1):
            for c in range(n - k + 1):

                curr = SortedList()
                for i in range(r, min(r + k, m)):
                    for j in range(c, min(c + k, n)):
                        if grid[i][j] not in curr:
                            curr.add(grid[i][j])
                diff = float("inf")
                if len(curr) == 1:
                    diff = 0
                else:
                    for i in range(len(curr) - 1):
                        first, second = curr[i], curr[i + 1]

                        diff = min(diff, abs(first - second))
                    
                ans[r][c] = diff
        
        return ans

