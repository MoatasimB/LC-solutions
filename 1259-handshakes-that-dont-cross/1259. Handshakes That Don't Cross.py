class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        n = numPeople // 2

        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
                dp[i] %= (1000000007)
        
        return dp[n]
        
        # return (int((1 / (n + 1)) * (math.comb(2*n, n) % (10**9 + 7)) )) % (10**9 + 7)


  
    [1,1,2]

    # i = 5

    # dp[0] * dp[4]
    # dp[1] * dp[3]
    # dp[2] * dp[2]
    # dp[3] * dp[1]
    # dp[4] * dp[0]