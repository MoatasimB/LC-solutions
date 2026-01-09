class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        

        curr_len = 1

        ans = 1

        for i in range(1, len(prices)):
            if prices[i] + 1 == prices[i - 1]:
                curr_len += 1
            else:
                curr_len = 1
            ans += curr_len
        
        return ans