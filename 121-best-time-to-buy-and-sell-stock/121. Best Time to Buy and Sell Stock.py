class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        currMin = float("inf")
        ans = 0
        for i in range(len(prices)):
            if prices[i] < currMin:
                currMin = prices[i]
                continue
            else:
                ans = max(ans, prices[i]-currMin)
        return ans