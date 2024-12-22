class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def dfs(i, holding):
            if (i,holding) in dp:
                return dp[(i, holding)]
            if i == len(prices):
                return 0
            
            ans = 0
            ans += dfs(i+1, holding)
            if holding:
                ans= max(ans, prices[i] + dfs(i+1, False))
            else:
                ans = max(ans, -prices[i] + dfs(i+1, True))
            
            dp[(i,holding)] = ans
            return ans
        
        return dfs(0,False)

