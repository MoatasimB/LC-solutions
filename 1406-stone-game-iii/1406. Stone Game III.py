class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        
        n = len(stoneValue)
        memo = {}
        def dfs(i):

            if i >= n:
                return 0
            if i in memo:
                return memo[i]
            curr = float("-inf")
            stones = 0
            for j in range(i, min(n, i + 3)):
                stones += stoneValue[j]
                curr = max(curr, stones - dfs(j + 1))
            
            memo[i] = curr
            return curr
        
        ans = dfs(0)
        print(ans)
        if ans > 0 :
            return "Alice"
        elif ans < 0:
            return "Bob"
        
        return "Tie"