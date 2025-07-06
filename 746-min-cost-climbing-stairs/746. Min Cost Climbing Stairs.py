class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)


        memo = [float('inf')] * (n + 1)

        memo[0] = 0
        memo[1] = 0

        for i in range(2, n + 1):
            memo[i] = min(cost[i - 1] + memo[i-1], cost[i-2] + memo[i-2])
        
        return memo[n]


        #C(n) = min cost to reach stair n
        #C(n) = min(C(n-1) + cost[n-1], C(n-2) + cost[n-2])
        #C(0) = 0, C(1) = 0
        # memo = {}
        # def dfs(i):
        #     if i in memo:
        #         return memo[i]
        #     if i <= 1:
        #         return 0
        #     memo[i] = min(cost[i - 1] + dfs(i-1), cost[i - 2] + dfs(i-2))
        #     return memo[i]
        
        # return dfs(n)