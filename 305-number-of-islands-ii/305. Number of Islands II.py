class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        def valid(r, c):
            return 0<= r < m and 0 <= c < n
        # r * n + c
        dirs = [(0, 1), (1,0), (0,-1), (-1,0)]

        class DSU:
            def __init__(self, size):
                self.roots = [i for i in range(size)]
                self.ranks = [0] * size
                self.islands = 0
                self.marked = [False] * size
            
            def find(self, x):
                if self.roots[x] == x:
                    return x
                
                self.roots[x] = self.find(self.roots[x])
                return self.roots[x]
            
            def addIsland(self, r, c):

                curr = r * n + c
                if self.marked[curr]:
                    return self.islands
                self.islands += 1
                self.marked[curr] = True
                
                for dx, dy in dirs:
                    nr = r + dx
                    nc = c + dy
                    if not valid(nr, nc):
                        continue
                    nei = nr * n + nc
                    if self.marked[nei]:
                        self.union(curr, nei)

                return self.islands

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
                    self.islands -= 1
        
        dsu = DSU(m*n)

        ans = []

        for r, c in positions:
            ans.append(dsu.addIsland(r,c))

        return ans