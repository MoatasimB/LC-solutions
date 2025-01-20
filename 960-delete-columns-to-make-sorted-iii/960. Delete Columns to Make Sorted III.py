class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        m = len(strs)
        n = len(strs[0])
        dp = {}
        def dfs(currCol, prevCol):
            if currCol == n:
                return 0
            
            if (currCol, prevCol) in dp:
                return dp[(currCol, prevCol)]
            
            ans = 1 + dfs(currCol + 1, prevCol)

            if prevCol == -1:
                ans = min(ans, dfs(currCol + 1, currCol))
            else:
                flag = True

                for i in range(m):
                    if strs[i][prevCol] <= strs[i][currCol]:
                        continue
                    else:
                        flag = False
                        break
                if flag:
                    ans = min(ans, dfs(currCol + 1, currCol))
            
            dp[(currCol, prevCol)] = ans
            return ans
        
        return dfs(0, -1)
