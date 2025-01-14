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
        
        prev = [False] * (len(s2) + 1)
        prev[0] = True
        
        for i in range(1, len(s2) + 1):
            if s2[i-1] == s3[i-1] and prev[i-1]:
                prev[i] = True
        for i in range(1, len(s1)+1):
            curr = [False] * (len(s2) + 1)
            # if s1[i-1] == s3[i-1]:
            #     curr[0] = True
            for j in range(len(s2)+1):
                up = False
                if s1[i-1] == s3[i+j-1]:
                    up = prev[j]
                left = False
                if j>0 and s2[j-1] == s3[i+j-1]:
                    left = curr[j-1]
                
                curr[j] = left or up
            print(curr)
            prev = curr
        return prev[len(s2)]