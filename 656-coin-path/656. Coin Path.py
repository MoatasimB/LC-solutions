class Solution:
    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:

        n = len(coins)
        dp = [float("inf")] * (n)
        dp[n - 1] = coins[n - 1]
        if coins[n - 1] == -1:
            return []
        nextA = [-1] * n

        for i in range(n - 2, -1, -1):
            if coins[i] == -1:
                continue
            for j in range(i + 1, min(i + maxJump + 1, n)):
                if coins[i] + dp[j] < dp[i]:
                    dp[i] = coins[i] + dp[j]
                    nextA[i] = j

        # print(dp, nextA)

        if dp[0] == float("inf"):
            return []
        
        
        ans = []
        i = 0
        while i != -1:
            ans.append(i + 1)
            i = nextA[i]
            
        
        return ans





        