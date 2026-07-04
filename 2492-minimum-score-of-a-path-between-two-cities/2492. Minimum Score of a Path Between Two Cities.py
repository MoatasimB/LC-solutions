class DSU:
    def __init__(self,size):
        self.ranks = [0] * size
        self.roots = [i for i in range(size)]

    def find(self, x):
        if self.roots[x] == x:
            return x
        
        self.roots[x] = self.find(self.roots[x])
        return self.roots[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX!=rootY:
            if self.ranks[rootX] > self.ranks[rootY]:
                self.roots[rootY] = rootX
            elif self.ranks[rootX] < self.ranks[rootY]:
                self.roots[rootX] = rootY
            else:
                self.roots[rootY] = rootX
                self.ranks[rootX] += 1
        

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        ans = float("inf")
        dsu = DSU(n)
        for a, b, _ in roads:
            dsu.union(a - 1, b - 1)
        
        for a, b, w in roads:
            if dsu.find(0) == dsu.find(a - 1):
                ans = min(ans, w)
        
        return ans

        
