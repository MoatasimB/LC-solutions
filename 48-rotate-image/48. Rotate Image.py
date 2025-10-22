class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for row in matrix:
            i = 0
            j = n - 1

            while i <= j:
                row[i], row[j] = row[j], row[i]
                i += 1
                j -= 1
        

