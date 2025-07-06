class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)



        one_back = 0
        two_back = 0
        curr = 0
        for i in range(2, n + 1):
            curr = min(cost[i - 1] + one_back, cost[i-2] + two_back)
            two_back = one_back
            one_back = curr
        
        return curr


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