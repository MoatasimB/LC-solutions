class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return sum(cost)
        cost.sort(reverse=True)
        n = len(cost)
        i = 0
        ans = 0
        while i + 1 < n:
            print(i, cost[i], cost[i + 1])
            buy =  cost[i] + cost[i + 1]
            ans += buy
            i = i + 3
        if i == n - 1:
            ans += cost[-1]
        return ans
