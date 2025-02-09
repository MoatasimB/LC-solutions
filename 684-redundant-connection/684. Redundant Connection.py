class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        seen = set()
        parent = {}
        cycle_start = -1
        def dfs(node):
            seen.add(node)
            nonlocal cycle_start

            for nei in adj[node]:
                if nei not in seen:
                    parent[nei] = node
                    dfs(nei)
                elif nei != parent[node] and cycle_start == -1:
                    cycle_start = nei
                    parent[nei] = node
        

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        dfs(1)

        cycle = {}
        curr = cycle_start

        while True:
            cycle[curr] = 1
            curr = parent[curr]
            if curr == cycle_start:
                break
        
        for i in range(len(edges)-1, -1, -1):
            u = edges[i][0]
            v = edges[i][1]
            if u in cycle and v in cycle:
                return edges[i]
        
        
        
        
        
        
        
        
        
        
        
        
        # class UF:
        #     def __init__(self, size):
        #         self.roots = [i for i in range(size)]
        #         self.ranks = [0] * size
            
        #     def find(self, x):
        #         if self.roots[x] == x:
        #             return x
                
        #         self.roots[x] = self.find(self.roots[x])
        #         return self.roots[x]
            
        #     def union(self, x, y):
        #         rootX = self.find(x)
        #         rootY = self.find(y)

        #         if rootX != rootY:

        #             if self.ranks[rootX] < self.ranks[rootY]:
        #                 self.roots[rootX] = rootY
        #             elif self.ranks[rootX] > self.ranks[rootY]:
        #                 self.roots[rootY] = rootX
        #             else:
        #                 self.roots[rootY] = rootX
        #                 self.ranks[rootX] +=1
        #             return True
        #         return False
        
        # n = len(edges)
        # uf = UF(n)

        # for u,v in edges:
        #     if not uf.union(u-1,v-1):
        #         return [u,v]

