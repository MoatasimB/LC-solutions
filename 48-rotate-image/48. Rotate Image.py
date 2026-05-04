class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])


        for i in range(m):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        

        for row in matrix:
            i = 0
            j = m - 1
            while i < j:
                row[i], row[j] = row[j], row[i]
                i += 1
                j -= 1
        