class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        class UF:

            def __init__(self, size):
                self.roots = [i for i in range(size)]
                self.par = [0] * size
                self.components = size
            def find(self, x):
                if x == self.roots[x]:
                    return x
                
                self.roots[x] = self.find(self.roots[x])

                return self.roots[x]
            
            def union(self, x, y):
                rootX = self.find(x)
                rootY = self.find(y)

                if rootX != rootY:

                    if self.par[rootX] > self.par[rootY]:
                        self.roots[rootY] = rootX
                    elif self.par[rootX] < self.par[rootY]:
                        self.roots[rootX] = rootY
                    else:
                        self.roots[rootY] = rootX
                        self.par[rootX] += 1
                    self.components -= 1
            
            def total_components(self):
                return self.components
        

        uf = UF(n)

        for x, y in edges:
            uf.union(x,y)
        
        return uf.total_components()