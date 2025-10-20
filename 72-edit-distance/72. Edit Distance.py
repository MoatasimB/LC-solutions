class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        memo = {}
        def dfs(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i == -1 and j == -1:
                return 0
            if i == -1:
                return j + 1
            if j == -1:
                return i + 1
            ans = 0
            if word1[i] == word2[j]:
                ans = dfs(i-1, j-1) 
            else:
                ans =  1 + min(dfs(i-1, j), dfs(i, j-1), dfs(i-1,j-1))
            memo[(i,j)] = ans
            return ans
        
        return dfs(n-1, m-1)

        
        # intention
        # execution