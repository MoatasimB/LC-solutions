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

        if rootX != rootY:
            if self.ranks[rootX] < self.ranks[rootY]:
                self.roots[rootX] = rootY
            elif self.ranks[rootY] < self.ranks[rootX]:
                self.roots[rootY] = rootX
            else:
                self.roots[rootY] = rootX
                self.ranks[rootX] += 1
    
class Solution:
    def maxActivated(self, points: list[list[int]]) -> int:

        x_axis = defaultdict(int)
        y_axis = defaultdict(int)


        n = len(points)

        dsu = DSU(n)

        for i in range(n):
            x, y = points[i]

            if x not in x_axis:
                x_axis[x] = i
            else:
                dsu.union(x_axis[x], i)

            if y not in y_axis:
                y_axis[y] = i
            else:
                dsu.union(y_axis[y], i)


        sizes = [0] * n

        for i in range(n):
            sizes[dsu.find(i)] += 1

        # print(sizes)

        first = 0
        second = 0

        for num in sizes:
            if num > first:
                second = first
                first = num
            elif num > second:
                second = num
        # print(first, second)
        return first + second + 1
            
        
                

        
        