class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        
        m = max(nums)
        n = len(nums)
        MOD = 10**9 + 7

        dp = [[[0] * (m + 1) for _ in range(m + 1)] for _ in range(n + 1)]
        dp[0][0][0] = 1

        for i in range(1, n + 1):
            for j in range(m + 1):
                for k in range(m + 1):
                    count = dp[i - 1][j][k]

                    dp[i][math.gcd(nums[i - 1], j)][k] += (count % MOD)
                    dp[i][j][math.gcd(nums[i - 1], k)] += (count % MOD)
                    dp[i][j][k] += (count % MOD)
        
        ans = 0
        for i in range(1, m + 1):
            ans += (dp[n][i][i] % MOD)
        
        return ans % MOD
