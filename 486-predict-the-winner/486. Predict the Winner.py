class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = nums[i]
        
        for size in range(1, n):
            for left in range(n - size):
                right = left + size
                dp[left][right] = max(nums[left] - dp[left + 1][right], nums[right] - dp[left][right - 1])
        
        return dp[0][n - 1] >= 0
        memo = {}
        def dfs(i, j):
            if i > j:
                return 0
            if i == j:
                return nums[i]
            if (i, j) in memo:
                return memo[(i, j)]
            
            score = float("-inf")
            curr = 0
            score = max(score, nums[i] - dfs(i + 1, j))
            score = max(score, nums[j] - dfs(i, j - 1))
            memo[(i, j)] = score
            return score
        
        n = len(nums)

        final = dfs(0, n - 1)
        return final >= 0
        