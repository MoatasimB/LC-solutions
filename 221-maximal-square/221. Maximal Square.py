class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        mat = [[0] * n for _ in range(m)]
        mat[0][0] = int(matrix[0][0])
        memo = {}
        def dfs(r,c):
            if (r,c) in memo:
                return memo[(r,c)]
            if r == 0 and c == 0:
                return int(matrix[r][c])
            
            if r < 0 or c < 0:
                return 0
            
            curr = matrix[r][c]
            top = dfs(r - 1, c)
            left = dfs(r, c - 1)
            diagonal = dfs(r-1, c-1)
            if int(curr) == 1:
                mat[r][c] = min(top, left, diagonal) + int(curr)
            memo[(r, c)] = mat[r][c]
            return mat[r][c]
        
        dfs(m-1, n-1)
        print(mat)
        return max(max(row) for row in mat) ** 2


        [
            ["1","0","1","1","0","1"],
            ["1","1","1","1","1","1"],
            ["0","1","1","0","1","1"],
            ["1","1","1","0","1","0"],
            ["0","1","1","1","1","1"],
            ["1","1","0","1","1","1"]]

        [
            [1, 0, 1, 1, 0, 1], 
            [1, 1, 1, 2, 1, 1], 
            [0, 1, 2, 1, 2, 2], 
            [1, 1, 2, 1, 2, 2], 
            [0, 1, 2, 2, 2, 3], 
            [1, 1, 1, 2, 3, 3]]