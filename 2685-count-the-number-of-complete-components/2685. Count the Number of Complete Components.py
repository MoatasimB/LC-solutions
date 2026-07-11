class DSU:
    def __init__(self, size):
        self.roots = [i for i in range(size)]
        self.ranks = [0] * size
    
    def find(self, x):
        if self.roots[x] == x:
            return x
        self.roots[x] = self.find(self.roots[x])
        return self.roots[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.ranks[rootX] < self.ranks[rootY]:
                self.roots[rootX] = rootY
            elif self.ranks[rootY] < self.ranks[rootX]:
                self.roots[rootY] = rootX
            else:
                self.ranks[rootY] += 1
                self.roots[rootX] = rootY

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        
        #cc : number of edges
        #cc : number of nodes

        dsu = DSU(n)

        for a, b in edges:
            dsu.union(a, b)
        
        components = defaultdict(int)
        edges_in_components = defaultdict(int)
        for i in range(n):
            parent = dsu.find(i)
            components[parent] += 1
        
        for a, b in edges:
            parent = dsu.find(a)
            edges_in_components[parent] += 1
        
        ans = 0

        for comp, nodes in components.items():
            if nodes == 1 or nodes == 2:
                ans += 1
                continue
            count = edges_in_components[comp]
            ans += (count == math.comb(nodes, 2))
        
        return ans

