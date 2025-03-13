class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        

        m = len(mat1)
        k = len(mat1[0])
        n = len(mat2[0])

        def getVal(r,c):
            ans = 0
            for i in range(k):
                ans += (mat1[r][i] * mat2[i][c])
            return ans
        
        final = [[0] * n for _ in range(m)]

        for row in range(m):
            for col in range(n):
                val = getVal(row,col)
                final[row][col] = val
        
        return final