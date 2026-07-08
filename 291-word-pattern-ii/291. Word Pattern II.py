class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        
        n = len(pattern)
        m = len(s)

        def dfs(i, j, mpp):
            if i == n and j == m:
                return len(set(mpp.values())) == len(set(pattern))
                
            if i == n or j == m:
                return False
            
            currCh = pattern[i]
            if currCh in mpp:
                mapping = mpp[currCh]
                length = len(mapping)
                if s[j:j + length] != mapping:
                    return False
                else:
                    return dfs(i + 1, j + length, mpp)
            else:
                for w in range(j, m):
                    match = s[j:w+1]
                    mpp[currCh] = match
                    # print(currCh, match, mpp, i, j)
                    if dfs(i + 1, w + 1, mpp):
                        return True
                    del mpp[currCh]
                return False
        

        return dfs(0, 0, {})
