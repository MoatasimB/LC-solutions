class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        

        #C(n) = min cost to reach stair n
        #C(n) = min(C(n-1) + cost[n-1], C(n-2) + cost[n-2])
        #C(0) = cost[0], C(1) = cost[1]
        memo = {}
        n = len(cost)
        def dfs(i):
            if i in memo:
                return memo[i]
            if i >= n:
                return 0
            memo[i] = min(cost[i] + dfs(i+1), cost[i] + dfs(i+2))
            return memo[i]
        
        return min(dfs(0), dfs(1))