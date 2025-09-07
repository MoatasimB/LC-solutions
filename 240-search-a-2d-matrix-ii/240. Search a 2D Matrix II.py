class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])
        
        def valid(r,c):
            return 0 <= r < m and 0 <= c < n

        
        r = m - 1
        c = 0


        while valid(r,c):

            if matrix[r][c] > target:
                r -= 1
            elif matrix[r][c] < target:
                c += 1
            else:
                return True
        
        return False
        
   
        


        
            
            
            
            
            