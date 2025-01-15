class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def dfs(i, holding, k):
            if (i,holding,k) in dp:
                return dp[(i,holding,k)]
            
            if k == -1:
                return 0
            if i == len(prices):
                return 0
            
            curr = float('-inf')
            if holding:
                curr = max(curr, prices[i] + dfs(i+1, False, k), dfs(i+1, True, k))
            
            else:
                curr = max(curr, dfs(i+1, False, k) ,dfs(i+1, True, k-1) - prices[i])
            dp[(i,holding,k)] = curr
            return curr
        
        return dfs(0, False, 2)