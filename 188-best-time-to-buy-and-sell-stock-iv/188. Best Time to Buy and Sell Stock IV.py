class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = {}

        def dfs(i, holding, k):
            if i==len(prices):
                return 0
            if k == -1:
                return 0
            if (i,holding,k) in dp:
                return dp[(i,holding,k)]
            
            curr = float('-inf')
            if holding:
                curr = max(curr, prices[i] + dfs(i+1, not holding, k), dfs(i+1, holding, k))
            else:
                curr = max(curr, dfs(i+1, holding, k), dfs(i+1, True, k-1) - prices[i])
            
            dp[(i,holding,k)] = curr
            return curr
        
        return dfs(0, False, k)