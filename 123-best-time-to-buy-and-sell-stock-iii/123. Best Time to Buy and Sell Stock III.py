class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        bestLeft = [0] * len(prices)
        bestRight = [0] * len(prices)

        left = prices[0]
        for i in range(1, len(bestLeft)):
            if prices[i] > left:
                bestLeft[i] = max(bestLeft[i-1], prices[i]-left)
            else:
                left = min(left, prices[i])
                bestLeft[i] = bestLeft[i-1]
        

        right = prices[-1]
        for i in range(len(bestRight)-2, -1, -1):
            if right > prices[i]:
                bestRight[i] = max(bestRight[i-1], right - prices[i])
            else:
                right = max(right, prices[i])
                bestRight[i] = bestRight[i-1]
        

        ans = 0

        for i in range(len(bestLeft)):
            ans = max(ans, bestLeft[i] + bestRight[i])
        
        return ans
        