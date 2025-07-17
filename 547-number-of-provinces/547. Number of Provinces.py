class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        class UnionFind:

            def __init__(self, size):
                self.roots =[i for i in range(size)]
                self.ranks = [0] * size
                self.components = size
            
            def find(self, x):
                if self.roots[x] == x:
                    return x
                
                self.roots[x] = self.find(self.roots[x])

                return self.roots[x]
            
            def union(self, x, y):
                rootX = self.find(x)
                rootY = self.find(y)

                if rootX != rootY:
                    self.components -= 1

                    if self.ranks[rootX] > self.ranks[rootY]:
                        self.roots[rootY] = rootX
                    elif self.ranks[rootY] > self.ranks[rootX]:
                        self.roots[rootX] = rootY
                    else:
                        self.roots[rootX] = rootY
                        self.ranks[rootY] += 1
            

        n = len(isConnected)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(i):
                if isConnected[i][j]:
                    uf.union(i,j)
        
        return uf.components

                