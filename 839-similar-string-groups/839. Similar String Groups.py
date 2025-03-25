class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        
        adj = defaultdict(list)

        for i in range(len(strs)):
            for j in range(i+1, len(strs)):
                word1 = strs[i]
                word2 = strs[j]
                diff = 0
                for k in range(len(word1)):
                    if word1[k] != word2[k]:
                        diff += 1
                    if diff > 2:
                        break
                
                if diff == 2:
                    adj[word1].append(word2)
                    adj[word2].append(word1)
        

        def dfs(word):
            seen.add(word)
            for nei in adj[word]:
                if nei not in seen:
                    dfs(nei)
        
        ans = 0
        seen = set()
        for i in range(len(strs)):
            if strs[i] not in seen:
                ans += 1
                dfs(strs[i])
        
        return ans
        

