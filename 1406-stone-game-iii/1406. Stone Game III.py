class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        memo = {}
        def dfs(i, player):
            if i >= len(stoneValue):
                return 0

            if (i, player) in memo:
                return memo[(i, player)]
            
            #each player can take up to 1-3 stones
            score = float("-inf") if player == 0 else float("inf")
            curr = 0
            for j in range(i, min(i + 3, len(stoneValue))):
                if player == 0:
                    curr += stoneValue[j]
                    score = max(score, curr + dfs(j + 1, 1))
                else:
                    curr -= stoneValue[j]
                    score = min(score, curr + dfs(j + 1, 0))
            
            memo[(i, player)] = score
            return score
        
        #Alice score;
        aliceScore = dfs(0,0)
        if aliceScore > 0:
            return "Alice"
        elif aliceScore < 0:
            return "Bob"

        return "Tie"

