class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = m - 1
        row = None
        while l < r:
            mid = (l + r) // 2
            if matrix[mid][-1] > target and matrix[mid][0] > target :
                r = mid - 1
    
            elif matrix[mid][-1] < target and matrix[mid][0] < target:
                l = mid + 1
                
            elif matrix[mid][-1] == target:
                return True
            else:
                row = mid
                break
        if row == None:
            row = l
        

        l = 0
        r = n - 1
        while l <= r:

            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False
