class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        class UF:
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
                    elif self.ranks[rootX] > self.ranks[rootY]:
                        self.roots[rootY] = rootX
                    else:
                        self.roots[rootY] = rootX
                        self.ranks[rootX] +=1
                    return True
                return False
        
        n = len(edges)
        uf = UF(n)

        for u,v in edges:
            if not uf.union(u-1,v-1):
                return [u,v]

