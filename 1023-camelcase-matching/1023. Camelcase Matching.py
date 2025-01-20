class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        
        def dfs(i,j,word, pattern, dp):

            if j == -1:
                for ch in word[:i+1]:
                    if ch.isupper():
                        return False
                return True
            
            if i <= -1 and j > -1:
                return False
            
            if (i,j) in dp:
                return dp[(i,j)]
            
            if word[i] == pattern[j]:
                if dfs(i-1, j-1, word, pattern, dp):
                    dp[(i,j)] = True
                    return True
            
            else:
                # if word[i].isupper():
                #     dp[(i,j)] = False
                #     return False
                if word[i].islower() and dfs(i-1, j, word, pattern, dp):
                    dp[(i,j)] = True
                    return True
            
            dp[(i,j)] = False
            return False
        
        ans = []
        n = len(pattern) - 1
        for query in queries:
            ans.append(dfs(len(query) - 1, n, query, pattern, {}))
        
        return ans
            
