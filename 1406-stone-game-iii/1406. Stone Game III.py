class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        memo = {}
        def dfs(i):
            if i >= len(stoneValue):
                return 0

            if i in memo:
                return memo[i]
            
            #each player can take up to 1-3 stones
            score = float("-inf")
            curr = 0
            for j in range(i, min(i + 3, len(stoneValue))):
                curr += stoneValue[j]
                score = max(score, curr - dfs(j + 1))
                
            
            memo[i] = score
            return score
        
        #Alice score;
        aliceScore = dfs(0)
        if aliceScore > 0:
            return "Alice"
        elif aliceScore < 0:
            return "Bob"

        return "Tie"

