class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i, j)]
            if i <= -1 and j <= -1:
                return 0
            if i <= -1:
                return j + 1
            if j <= -1:
                return i + 1

            if word1[i] == word2[j]:
                dp[(i,j)] = dfs(i - 1, j - 1)
                return dp[(i, j)]
            else:
                dp[(i,j)] = 1 + min(dfs(i - 1, j), dfs(i, j - 1), dfs(i - 1, j - 1))
                return dp[(i, j)]
        
        dp = {}
        return dfs(len(word1) - 1, len(word2) - 1)

#     sea
#     eat

# 1+ 
#     sea
#     ea

#     se
#     e

#     s


    
