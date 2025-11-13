class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        memo = {}
        def dp(r,c, cost):
            cost += grid[r][c] if grid[r][c] == 0 else 1
            
            if cost > k:
                return float("-inf") 
            if (r,c, cost) in memo:
                return memo[(r,c, cost)]
            if r < 0 or c < 0:
                return float("-inf")
       
            if r == 0 and c == 0:
                return grid[0][0]


            


            up  = dp(r - 1, c, cost)
            left = dp(r, c - 1, cost)


            ans = max(left, up)
            if ans != float("-inf"):
                ans += grid[r][c]
                
            memo[(r,c, cost)] = ans
            return ans

        final = dp(m-1, n-1, 0)
        return final if final != float("-inf") else -1


       # [
       #     [0, 1, 1, 1],
       #     [1, 2, 2, 0],
       #     [1, 0, 1, 2]
       # ]

       #  cost = 1 , score = 2 , cell = (2,3)

        # {(0, 1, 4): 1, 
        #  (0, 2, 3): 2, 
        #  (0, 3, 2): 3, 
        #  (1, 0, 4): 1, 
        #  (1, 1, 3): 3, 
        #  (1, 2, 2): 5, 
        #  (1, 3, 1): 5, 
        #  (2, 0, 3): 2, 
        #  (2, 1, 2): 3, 
        #  (2, 2, 2): 6, 
        #  (2, 3, 1): 8}