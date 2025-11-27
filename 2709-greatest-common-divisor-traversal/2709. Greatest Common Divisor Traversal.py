class DSU:
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

        if rootX != rootY:
            if self.ranks[rootX] < self.ranks[rootY]:
                self.roots[rootX] = rootY
            elif self.ranks[rootY] < self.ranks[rootX]:
                self.roots[rootY] = rootX
            else:
                self.roots[rootX] = rootY
                self.ranks[rootY] += 1
            self.components -= 1

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        uf = DSU(len(nums))

        #we have a mpp prime factor to idx
        #this means there is an element in nums at idx with this prime factor
        #if we find another idx with this prime factor we will union it

        factors = {} #factor : first idx to have it (all later idx will merge with this one)

        for i, num in enumerate(nums):

            f = 2

            while f * f <= num:

                if num % f == 0:
                    if f in factors:
                        uf.union(i, factors[f])
                    else:
                        factors[f] = i
                
                    while num % f == 0:
                        num = num // f #take that entire factor out
                
                f += 1
            
            if num > 1:
                if num in factors:
                    uf.union(i, factors[num])
                else:
                    factors[num] = i
        

        if uf.components == 1:
            return True
        
        return False