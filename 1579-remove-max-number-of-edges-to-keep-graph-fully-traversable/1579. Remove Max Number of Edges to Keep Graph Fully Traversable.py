class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges.sort(reverse=True)
        class UnionFind:

            def __init__(self, size):
                self.roots = [i for i in range(size)]
                self.ranks = [0] * size
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
                    if self.ranks[rootX] < self.ranks[rootY]:
                        self.roots[rootX] = rootY
                    elif self.ranks[rootY] < self.ranks[rootX]:
                        self.roots[rootY] = rootX
                    else:
                        self.roots[rootY] = rootX
                        self.ranks[rootX] += 1
                    self.components -= 1
                    return True
                
                return False
            
            def traversable(self):
                return self.components == 1
            
            def isConnected(self, x, y):
                return self.find(x) == self.find(y)
        

        alice = UnionFind(n)
        bob = UnionFind(n)

        ans = 0
        for t, u, v in edges:
            u = u - 1
            v = v - 1
            if t == 1:
                if not alice.union(u,v):
                    ans +=1
            elif t == 2:
                if not bob.union(u,v):
                    ans +=1
            elif t == 3:
                x = bob.union(u,v)
                y = alice.union(u,v)
                if not x and not y:
                    ans +=1
        
        if not alice.traversable() or not bob.traversable():
            return -1
 
        return ans



