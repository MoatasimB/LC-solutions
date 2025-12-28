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
            l = 0
            r = n - 1

            while l < r :
                row[l], row[r] = row[r], row[l]
                l += 1
                r -= 1
        
