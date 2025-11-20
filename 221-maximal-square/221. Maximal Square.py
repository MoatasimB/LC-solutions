class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        mat = [[0] * n for _ in range(m)]
        mat[0][0] = int(matrix[0][0])

        mat = [int(x) for x in matrix[0]]
        mat[0] = int(matrix[0][0])
        ans = max(mat)
        for r in range(1, m):
            new_mat = [0] * n
            for c in range(n):

                top = 0
                left = 0
                diagonal = 0
                if r > 0:
                    top = mat[c]
                if c > 0:
                    left = new_mat[c - 1]
                if r > 0 and c > 0:
                    diagonal = mat[c-1]
                
                curr = int(matrix[r][c])
                if curr == 1:
                    new_mat[c] = min(top, left, diagonal) + 1
       
                ans = max(ans, new_mat[c])
            
            mat = new_mat
        
        return ans ** 2
        


        # memo = {}
        # def dfs(r,c):
        #     if (r,c) in memo:
        #         return memo[(r,c)]
        #     if r == 0 and c == 0:
        #         return int(matrix[r][c])
            
        #     if r < 0 or c < 0:
        #         return 0
            
        #     curr = matrix[r][c]
        #     top = dfs(r - 1, c)
        #     left = dfs(r, c - 1)
        #     diagonal = dfs(r-1, c-1)
        #     if int(curr) == 1:
        #         mat[r][c] = min(top, left, diagonal) + int(curr)
        #     memo[(r, c)] = mat[r][c]
        #     return mat[r][c]
        
        # dfs(m-1, n-1)
        # return max(max(row) for row in matrix) ** 2


    