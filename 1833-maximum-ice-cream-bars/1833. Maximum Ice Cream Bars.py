class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        ans = 0

        costs = sorted(costs)

        curr = 0
        for i in range(len(costs)):
            curr += costs[i]

            if curr > coins:
                break
            
            ans +=1
        
        return ans
        