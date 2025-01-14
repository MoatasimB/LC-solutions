class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}
        if len(s1) + len(s2) != len(s3):
            return False
        def dfs(i,j,c):
            if (i,j,c) in dp:
                return dp[(i,j,c)]       
            
            if i == -1 and j == -1 and c == -1:
                dp[(i,j,c)] = True
                return True
            if i >=0 and s1[i] == s3[c]:
                if dfs(i-1, j, c-1):
                    dp[(i,j,c)] = True
                    return True
            
            if j>=0 and s2[j] == s3[c]:
                if dfs(i, j-1, c-1):
                    dp[(i,j,c)] = True
                    return True
            
            dp[(i,j,c)] = False
            return False
            
        return dfs(len(s1)-1, len(s2)-1, len(s3)-1)