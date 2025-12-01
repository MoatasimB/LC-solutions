class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        curr_min = float("inf")

        ans = float("-inf")

        for i in range(len(prices)):
            if prices[i] < curr_min:
                curr_min = prices[i]
            else:
                ans = max(ans, prices[i] - curr_min)
        
        return ans if ans != float("-inf") else 0