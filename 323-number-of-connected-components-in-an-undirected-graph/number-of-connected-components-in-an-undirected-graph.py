class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = defaultdict(list)

        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
        
        seen = set()
        def dfs(node):
            seen.add(node)
            for nei in adj[node]:
                if nei not in seen:
                    dfs(nei)
        
        ans = 0
        single = n - len(adj.keys())
        for node in adj.keys():
            if node not in seen:
                ans +=1 
                dfs(node)
        
        return ans + single
            