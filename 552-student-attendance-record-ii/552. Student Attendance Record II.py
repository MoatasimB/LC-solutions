class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        memo = [[[-1] * 3 for _ in range(2)] for _ in range(n + 1)]
        def dfs(n, absences, consecutive_lates):
            if absences >= 2 or consecutive_lates >= 3:
                return 0

            if memo[n][absences][consecutive_lates] != -1:
                return memo[n][absences][consecutive_lates]
            
            
            if n == 0:
                return 1
            
            p = dfs(n - 1,absences, 0) % MOD
            a = dfs(n - 1,absences + 1, 0) % MOD
            l = dfs(n - 1,absences, consecutive_lates + 1) % MOD

            ans = (p + a + l) % MOD
            memo[n][absences][consecutive_lates] = ans
            return ans
        
        return dfs(n, 0, 0)
            
            