class UnionFind:
    def __init__(self, size):
        self.roots = [i for i in range(size)]
        self.ranks = [1] * size
        self.components = size
    
    def find(self, x):
        if self.roots[x] == x:
            return x
        self.roots[x] = self.find(self.roots[x])
        return self.roots[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False
        
        if self.ranks[rootX] < self.ranks[rootY]:
            self.roots[rootX] = rootY
        elif self.ranks[rootY] < self.ranks[rootX]:
            self.roots[rootY] = rootX
        else:
            self.roots[rootX] = rootY
            self.ranks[rootY] += 1
        self.components -= 1
        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        edges = [[edge[0], edge[1], edge[2], i] for i, edge in enumerate(edges)]

        edges.sort(key = lambda x: x[2])

        #first calculate standard MST
        uf = UnionFind(n)
        std_weight = 0
        for u, v, weight, idx in edges:
            if uf.union(u,v):
                std_weight += weight
        
        #Now go through all the edges and either ignore it or use it

        #if we ignore it and our MST is either disconnected or > total weight -> critical

        #if we force it and we have the same total weight => pseudo (if it is already critical we dont do this step)

        critical = []
        pseudoCritical = []

        for u, v, weight, idx in edges:

            #Ignore

            uf_ignore = UnionFind(n)
            ignore_weight = 0
            for x, y, w, j in edges:
                if idx == j: #this is the edge we are ignoring
                    continue
                if uf_ignore.union(x, y):
                    ignore_weight += w
            
            #check if it is critical
            if ignore_weight > std_weight or uf_ignore.components != 1:
                critical.append(idx)
                continue


            #Force
            uf_force = UnionFind(n)
            uf_force.union(u,v)
            force_weight = weight
            for x, y, w, j in edges:
                if idx == j: #this is the edge we already added
                    continue
                if uf_force.union(x, y):
                    force_weight += w
            
            if force_weight == std_weight:
                pseudoCritical.append(idx)
        

        return [critical, pseudoCritical]

        
