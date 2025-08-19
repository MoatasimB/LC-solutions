class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        s = list(s)
        graph = defaultdict(list)

        for x, y in pairs:
            graph[x].append(y)
            graph[y].append(x)
        
        

        def dfs(node):
            curr.append(s[node])
            curr_idx.append(node)
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei)
            
        seen = set()
        for x, y in pairs:
            curr = []
            curr_idx = []
            if x not in seen:
                seen.add(x)
                dfs(x)
            
                if curr:
                    curr.sort()
                    curr_idx.sort()
                    for i in range(len(curr)):
                        s[curr_idx[i]] = curr[i]
        
        return "".join(s)