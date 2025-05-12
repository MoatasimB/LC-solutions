class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        
        n = len(s1)
        m = len(s2)

        memo = {}
        def dfs(i,j,skip):
            if i == n and j == m:
                return skip == 0
    
            if (i,j,skip) in memo:
                return memo[(i,j,skip)]
            
            if i < n and s1[i].isdigit():
                num = 0
                k = i
                while k < n and s1[k].isdigit():
                    num = (num * 10) + int(s1[k])
                    k += 1
                    if dfs(k, j, skip - num):
                        memo[(i,j,skip)] = True
                        return True
            
            elif j < m and s2[j].isdigit():
                num = 0
                k = j
                while k < m and s2[k].isdigit():
                    num = (num * 10) + int(s2[k])
                    k += 1
                    if dfs(i, k, skip + num):
                        memo[(i,j,skip)] = True
                        return True
            
            elif skip == 0:
                if i < n and j < m and s1[i] == s2[j]:
                    return dfs(i+1,j+1,skip)
            
            elif skip < 0:
                if j < m:
                    return dfs(i, j+1, skip + 1)
            elif skip > 0:
                if i < n:
                    return dfs(i+1, j, skip - 1)
            
            memo[(i,j,skip)] = False
            return False
        
        return dfs(0,0,0)

