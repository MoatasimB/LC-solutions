class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}
        if len(s1) + len(s2) != len(s3):
            return False
        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
  
  
            if i == -1 and j == -1 :
                dp[(i,j)] = True
                return True
            
            if i >=0 and s1[i] == s3[i + j + 1]:
                if dfs(i-1, j):
                    dp[(i,j)] = True
                    return True
            
            if j>=0 and s2[j] == s3[i + j + 1]:
                if dfs(i, j-1):
                    dp[(i,j)] = True
                    return True
            
            dp[(i,j)] = False
            return False
            
        return dfs(len(s1)-1, len(s2)-1)