class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m = len(matrix)
        n = len(matrix[0])

        row1 = False

        for r in range(m):
            for c in range(n):
                if r == 0 and matrix[r][c] == 0:
                    row1 = True
                else:
                    if matrix[r][c] == 0:
                        matrix[0][c] = 0
                        matrix[r][0] = 0
        
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        

        if matrix[0][0] == 0:
            for r in range(m):
                matrix[r][0] = 0
        
        if row1:
            for c in range(n):
                matrix[0][c] = 0
        