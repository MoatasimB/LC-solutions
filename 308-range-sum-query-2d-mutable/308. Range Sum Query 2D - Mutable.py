class BitTree:
    def __init__(self, matrix):
        self.matrix = matrix
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.tree = [[0] * (self.n + 1) for _ in range(self.m + 1)]

        for r in range(self.m):
            for c in range(self.n):
                self.update(r, c, self.matrix[r][c])
    
    def update(self, i, j, val):

        i += 1
        while i <= self.m:
            c = j + 1
            while c <= self.n:
                self.tree[i][c] += val
                c += c & -c
            i += i &-i
    
    def prefix(self, r, c):
        i = r + 1
        ans = 0
        while i > 0:
            j = c + 1
            while j > 0:
                ans += self.tree[i][j]
                j -= j & -j
            i -= i & -i
        return ans


    def query(self, r1, c1, r2, c2):
        return self.prefix(r2, c2) - self.prefix(r1 - 1, c2) - self.prefix(r2, c1 - 1) + self.prefix(r1 - 1, c1 - 1)


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.bitTree = BitTree(matrix)
        self.matrix = matrix

    def update(self, row: int, col: int, val: int) -> None:
        
        og = self.matrix[row][col]
        delta = val - og
        self.matrix[row][col] = val
        self.bitTree.update(row, col, delta)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.bitTree.query(row1, col1, row2, col2)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)