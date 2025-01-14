class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # dp = {}
        if len(s1) + len(s2) != len(s3):
            return False
        
        # def dfs(i,j):
        #     if (i,j) in dp:
        #         return dp[(i,j)]
  
  
        #     if i == -1 and j == -1 :
        #         dp[(i,j)] = True
        #         return True
            
        #     if i >=0 and s1[i] == s3[i + j + 1]:
        #         if dfs(i-1, j):
        #             dp[(i,j)] = True
        #             return True
            
        #     if j>=0 and s2[j] == s3[i + j + 1]:
        #         if dfs(i, j-1):
        #             dp[(i,j)] = True
        #             return True
            
        #     dp[(i,j)] = False
        #     return False
            
        # return dfs(len(s1)-1, len(s2)-1)

        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]

        dp[0][0] = True

        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i==0 and j == 0:
                    continue
                
                up = False
                if i > 0 and s1[i-1] == s3[i+j-1]:
                    up = dp[i-1][j]
                
                left = False
                if j > 0 and s2[j-1] == s3[i+j-1]:
                    left = dp[i][j-1]
                
                dp[i][j] = left or up
        
        return dp[len(s1)][len(s2)]