class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
        for row in range(len(matrix)):
            i = 0
            j = len(matrix[0]) - 1

            while i <= j:
                matrix[row][i],matrix[row][j] = matrix[row][j],matrix[row][i]
                i +=1
                j -=1
        


