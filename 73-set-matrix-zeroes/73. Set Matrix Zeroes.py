class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix)
        n = len(matrix[0])

        col0 = 1

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if j == 0:
                        col0 = 0
                        matrix[i][0] = 0
                    else:
                        matrix[0][j] = 0
                        matrix[i][0] = 0
        x = matrix[0][0]
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for i in range(n):
                matrix[0][i] = 0
        if col0 == 0:
            for i in range(m):
                matrix[i][0] = 0
        

        