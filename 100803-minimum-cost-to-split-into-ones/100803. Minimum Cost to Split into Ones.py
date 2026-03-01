class Solution:
    def minCost(self, n: int) -> int:

        memo = {}
        def dfs(n):
            if n in memo:
                return memo[n]
            if n == 1:
                return 0

            cost = float("inf")
            for i in range(1, (n // 2) + 1):
                a = i
                b = n - i
                cost = min(cost, (a * b) + dfs(a) + dfs(b))
            memo[n] = cost
            return cost
        return dfs(n)