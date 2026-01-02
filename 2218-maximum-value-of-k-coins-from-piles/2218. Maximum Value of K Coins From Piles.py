class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        memo = {}
        def dfs(i, k):
            if (i, k) in memo:
                return memo[(i, k)]

            if k == 0 or i == len(piles):
                return 0
            
            
            curr = 0
            ans = dfs(i + 1, k)
            for j in range(min(len(piles[i]), k)):
                curr += piles[i][j]
                ans = max(ans, curr + dfs(i + 1, k - j - 1))

            memo[(i, k)] = ans
            return ans
        
        return dfs(0, k)
