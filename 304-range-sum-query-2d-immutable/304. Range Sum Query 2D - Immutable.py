class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.n = len(matrix)
        self.m = len(matrix[0])
        
        self.mat = [[0] * self.m for _ in range(self.n)]

        for r in range(self.n):
            for c in range(self.m):
                left = 0
                top = 0
                diagonal = 0
                curr = matrix[r][c]
                if c > 0:
                    left = self.mat[r][c - 1]
                if r > 0:
                    top = self.mat[r - 1][c]
                if r > 0 and c > 0:
                    diagonal = self.mat[r - 1][c - 1]
                self.mat[r][c] = curr + left + top - diagonal
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        top = self.mat[row1 - 1][col2] if row1 > 0 else 0
        left = self.mat[row2][col1 - 1] if col1 > 0 else 0
        diagonal = self.mat[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
        curr = self.mat[row2][col2]

        return curr - top - left + diagonal


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)