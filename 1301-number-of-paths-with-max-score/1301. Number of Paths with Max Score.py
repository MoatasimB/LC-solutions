class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:


        [
            "E5",
            "XS"
        ]


        MOD = 10**9 + 7
        m = len(board)
        n = len(board[0])

        dp1 = [[float("-inf")] * n for _ in range(m)]
        dp1[0][0] = 0
        for r in range(m):
            for c in range(n):
                if (r, c) == (0, 0) or board[r][c] == "X":
                    continue
                
                left = float("-inf")
                up = float("-inf")
                diagonal = float("-inf")
                curr = int(board[r][c]) if board[r][c] != "S" else 0
                if r - 1 >= 0:
                    up = dp1[r - 1][c]
                if r - 1 >= 0 and c - 1 >= 0:
                    diagonal = dp1[r - 1][c - 1]
                if c - 1 >= 0:
                    left = dp1[r][c - 1]
                dp1[r][c] = max(up, left, diagonal) + curr
        
        maxScore = dp1[m - 1][n - 1]
        if maxScore == float("-inf"):
            return [0,0]

        dp2 = [[0] * n for _ in range(m)]
        dp2[0][0] = 1

        for r in range(m):
            for c in range(n):
                if (r, c) == (0, 0) or board[r][c] == "X":
                    continue
                
    
                curr = int(board[r][c]) if board[r][c] != "S" else 0

                if r - 1 >= 0 and curr + dp1[r - 1][c] == dp1[r][c]:
                    dp2[r][c] += dp2[r - 1][c]% MOD
                if r - 1 >= 0 and c - 1 >= 0 and curr + dp1[r - 1][c - 1] == dp1[r][c]:
                    dp2[r][c] += dp2[r - 1][c - 1]% MOD
                if c - 1 >= 0 and curr + dp1[r][c - 1] == dp1[r][c]:
                    dp2[r][c] += dp2[r][c - 1]% MOD
        count = dp2[m - 1][n - 1] % MOD

        return [maxScore, count]
        