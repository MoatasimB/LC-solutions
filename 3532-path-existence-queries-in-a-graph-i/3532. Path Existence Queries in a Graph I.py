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

        if rootX == rootY:
            return
        
        if self.ranks[rootX] < self.ranks[rootY]:
            self.roots[rootX] = rootY
        elif self.ranks[rootY] < self.ranks[rootX]:
            self.roots[rootY] = rootX
        else:
            self.ranks[rootY] += 1
            self.roots[rootX] = rootY
    
    def isConnected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:

        idx_nums = [[x, i] for i, x in enumerate(nums)]

        idx_nums.sort()
        dsu = DSU(n)
        for i in range(1, n):
            prevNum, prevIdx = idx_nums[i - 1]
            currNum, currIdx = idx_nums[i]

            if abs(prevNum - currNum) <= maxDiff:
                dsu.union(prevIdx, currIdx)
        

        return [dsu.isConnected(x, y) for x, y in queries]


        