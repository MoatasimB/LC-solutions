class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        ans = []
        def dfs(i, curr, prev):
            if i == len(s):
                if curr in wordDict:
                    ans.append(prev + curr) 
                return
            
            if curr in wordDict:
                dfs(i, "", prev + curr + " ")
            
            dfs(i+1, curr + s[i], prev)
            
        
        dfs(0, "", "")

        return ans




        
