class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)

        for pile in piles:
            for j in range(1, len(pile)):
                pile[j] += pile[j-1]

        dp = {}
        def dfs(i, k):

            if i == n:
                return 0
            if k == 0:
                return 0
            if (i,k) in dp:
                return dp[(i,k)]
            ans = 0
            for j in range(len(piles[i])):
                if j + 1 <= k:
                    ans = max(ans, piles[i][j] + dfs(i+1, k-j-1))
            ans = max(ans, dfs(i+1, k))
            dp[(i,k)] = ans
            return ans
        
        return dfs(0,k)