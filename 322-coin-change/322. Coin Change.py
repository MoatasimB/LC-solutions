class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = {}

        def dfs(n):
            if n == 0:
                return 0
            if n < 0:
                return float('inf')
            
            if n in dp:
                return dp[n]
            
            curr = float('inf')
            for c in coins:
                curr = min(curr, 1 + dfs(n-c))
            
            dp[n] = curr

            return dp[n]
        
        x = dfs(amount)
        return x if x != float('inf') else -1
