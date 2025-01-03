class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid)
        n = len(grid[0])

        class UnionFind:
            def __init__(self, size):
                self.roots = [i for i in range(size)]
                self.ranks = [0] * size
                self.islands = 0
            

            def find(self, x):
                if self.roots[x] == x:
                    return x
                
                self.roots[x] = self.find(self.roots[x])

                return self.roots[x]
            
            def union(self, x,y):
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
                
                    self.islands -=1 
            
            def valid(self, r,c):
                return 0<=r<m and 0<=c<n
            
            def addLand(self, r,c):
                self.islands +=1

                dirs = [(0,1), (0,-1), (1,0), (-1,0)]

                for dx, dy in dirs:
                    new_r=dx + r
                    new_c=dy + c
                    if self.valid(new_r, new_c) and grid[new_r][new_c] == "1":
                        self.union(r*n + c, new_r*n + new_c)
            
            def isConnected(self, x,y):
                return self.find(x) == self.find(y)
            
            def getIslands(self):
                return self.islands
    
        uf = UnionFind(m*n)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    uf.addLand(i,j)
        
        return uf.getIslands()






        