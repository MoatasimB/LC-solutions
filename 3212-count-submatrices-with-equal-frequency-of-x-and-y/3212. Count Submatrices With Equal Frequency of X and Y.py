class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        

        check = defaultdict(bool) #matrix ending cell: contains X

        m = len(grid)
        n = len(grid[0])

        mat = [[float("inf")] * n for _ in range(m)]
        ans = 0
        for r in range(m):
            for c in range(n):
                up = mat[r-1][c] if r -1 >=0 else 0
                left = mat[r][c - 1] if c -1 >=0 else 0
                diag = mat[r-1][c - 1] if r -1 >=0 and c - 1 >= 0 else 0
                curr = 0
                if grid[r][c] == "X":
                    curr = -1
                elif grid[r][c] == "Y":
                    curr = 1
                
                if grid[r][c] == "X" or check[(r-1, c)] or check[(r-1, c - 1)] or check[(r, c - 1)]:
                    check[(r, c)] = True
                else:
                    check[(r, c)] = False
                mat[r][c] = left + up - diag + curr

                if mat[r][c] == 0 and check[(r, c)]:
                    ans += 1
        
        return ans

                

               
