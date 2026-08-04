class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        n = len(piles)
        memo = {}
        def dfs(i, j):
            if i == j:
                return piles[i]
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            memo[(i, j)] = max(piles[i] - dfs(i + 1, j), piles[j] - dfs(i, j - 1))
            return memo[(i, j)]
        
        return dfs(0, n - 1) > 0