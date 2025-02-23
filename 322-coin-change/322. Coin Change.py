class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # dp = {}

        # def dfs(n):
        #     if n == 0:
        #         return 0
        #     # if n < 0:
        #     #     return float('inf')
            
        #     if n in dp:
        #         return dp[n]
            
        #     curr = float('inf')
        #     for c in coins:
        #         if n - c >= 0:
        #             curr = min(curr, 1 + dfs(n-c))
            
        #     dp[n] = curr

        #     return dp[n]
        
        # x = dfs(amount)
        # return x if x != float('inf') else -1

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):

            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i],  1 + dp[i-c])

        return dp[amount] if dp[amount] != float('inf') else -1


        # 0 1 2 3 4 5 6 7 8 9 10 11
        # 0 1