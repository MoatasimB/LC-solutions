class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        
        adj = defaultdict(list)

        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
        
        ans = 0
        seen = set()
        A = None
        farthest = 0
        def dfs(node, dist):
            nonlocal A, farthest
            seen.add(node)
            if dist > farthest:
                farthest = dist
                A = node
            for nei in adj[node]:
                if nei not in seen:
                    dfs(nei, dist + 1)
        
        

        dfs(0, 0)
        print(A)
        start = A
        A = None
        farthest = 0
        seen = set()
        dfs(start, 0)
        print(A)
        return farthest
            

