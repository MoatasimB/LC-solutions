class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        
        class UnionFind:
            def __init__(self, size):
                self.roots = [i for i in range(size)]
                self.ranks = [0] * size
                self.comps = size
            
            def find(self, x):
                if self.roots[x] == x:
                    return x
                
                self.roots[x] = self.find(self.roots[x])

                return self.roots[x]

            def union(self, x, y):
                rootX = self.find(x)
                rootY = self.find(y)

                if rootX != rootY:
                    
                    if self.ranks[rootX] > self.ranks[rootY]:
                        self.roots[rootY] = rootX
                    elif self.ranks[rootY] > self.ranks[rootX]:
                        self.roots[rootX] = rootY
                    else:
                        self.roots[rootX] = rootY
                        self.ranks[rootY] += 1
                    self.comps -= 1
                
                return self.comps == 1
        

        uf = UnionFind(n)
        logs.sort()
        for timestamp, x, y in logs:
            if uf.union(x,y):
                return timestamp
        
        return -1

                
