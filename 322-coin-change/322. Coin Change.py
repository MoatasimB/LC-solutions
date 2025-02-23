class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def dfs(i, total):
            if total == 0:
                return 0
            if total < 0 or i == len(coins):
                return float('inf')
            if (i,total) in dp:
                return dp[(i, total)]
          
            if coins[i] <= total:
                take = 1 + dfs(i, total - coins[i])
            else:
                take = float('inf')
            notTake = dfs(i + 1, total)

            ans = min(take, notTake)
            dp[(i, total)] = ans
            return ans
        x = dfs(0, amount)
        return x if x != float('inf') else -1
