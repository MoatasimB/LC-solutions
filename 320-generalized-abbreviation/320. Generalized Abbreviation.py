class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        
        ans = []
        n = len(word)
        def dfs(i, curr):
            if i >= n:
                ans.append("".join(curr[:]))
                return
            
            for j in range(i, n):
                count = j - i + 1
                curr.append(str(count))
                if j + 1 < n:
                    curr.append(word[j + 1])
                dfs(j + 2, curr)
            
                if j + 1 < n:
                    curr.pop()
                curr.pop()
                
                
                curr.append(word[i:j + 1])
                dfs(j + 1, curr)
                curr.pop()
        
        dfs(0, [])
        return list(set(ans))