class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        dp = {}
        def dfs(i, target):
            if (i, target) in dp:
                return dp[(i, target)]
            if i == n:
                if target == 0:
                    return 1
                else:
                    return 0
            
            ans = 0
            for j in range(1, k+1):
                if target - j >= 0:
                    ans += dfs(i+1, target - j)

            dp[(i, target)] = ans % (10**9 + 7)
            return dp[(i, target)]

        return dfs(0,target)
