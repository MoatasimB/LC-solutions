class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for r, row in enumerate(matrix):
            i = 0
            j = len(row) - 1

            while i<=j:
                matrix[r][i], matrix[r][j] = matrix[r][j], matrix[r][i]
                i += 1
                j -= 1
        
        