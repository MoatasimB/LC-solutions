class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        

        m = len(coins)
        n = len(coins[0])

        dp = [[[float("-inf")] * 3 for _ in range(n)]for _ in range(m)]
        
        
        dp[0][0][0] = coins[0][0]
        for k in range(1, 3):
            dp[0][0][k] = max(coins[0][0], 0)

        for r in range(m):
            for c in range(n):
                for k in range(3):
                    if r == 0 and c == 0:
                        continue
                    
                    up = dp[r - 1][c][k] if r - 1 >= 0 else float("-inf")
                    left = dp[r][c - 1][k] if c - 1 >= 0 else float("-inf")
                    ans = coins[r][c] + max(up, left)
                    if coins[r][c] < 0 and k > 0:
                        up2 = dp[r - 1][c][k - 1] if r - 1 >= 0 else float("-inf")
                        left2 = dp[r][c - 1][k - 1] if c - 1 >= 0 else float("-inf")
                        ans = max(ans, up2, left2)
                
                    dp[r][c][k] = ans

        return dp[m - 1][n - 1][2]

        print(dp)
        memo = {}
        def dfs(r, c, k):
            if (r, c, k) in memo:
                return memo[(r, c, k)]
            if r == 0 and c == 0:
                if coins[r][c] < 0 and k > 0:
                    return 0
                else:
                    return coins[r][c]
            
            if r < 0 or c < 0:
                return float("-inf")

            
        
            up = dfs(r - 1, c, k)
            left = dfs(r, c - 1, k)
            ans = coins[r][c] + max(up, left)
            if coins[r][c] < 0 and k > 0:
                ans = max(ans, dfs(r - 1, c, k - 1), dfs(r, c - 1, k - 1))

            memo[(r, c, k)] = ans
            return ans
        
        return dfs(m - 1, n - 1, 2)
