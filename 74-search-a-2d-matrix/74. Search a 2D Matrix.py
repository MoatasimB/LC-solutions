class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1

        m = len(matrix)
        n = len(matrix[0])
        row = 0
        while top <= bottom:
            mid = (top + bottom) // 2

            if matrix[mid][0] < target:
                if target <= matrix[mid][n-1]:
                    row = mid
                    break
                else:
                    top = mid + 1
            elif matrix[mid][0] > target:
                bottom = mid - 1
            else:
                return True
        
        l = 0
        r = n - 1
        while l<=r:
            mid = (l+r) // 2


            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True
        return False


