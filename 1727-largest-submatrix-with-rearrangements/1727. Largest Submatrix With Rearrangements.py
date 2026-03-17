class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0])

        prev = []
        ans = 0
        for row in matrix:
            curr = []
            seen = [False] * n

            for height, col in prev:
                if row[col] == 1:
                    curr.append([height + 1, col])
                    seen[col] = True
            
            for i in range(n):
                if seen[i] == False and row[i] == 1:
                    curr.append([1, i])
            
            for i in range(len(curr)):
                ans = max(ans, curr[i][0] * (i + 1))

            prev = curr

        return ans





        heights = [[0] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 1:
                    heights[r][c] = 1 + (heights[r - 1][c] if r - 1 >= 0 else 0)
        
        ans = 0
        for row in heights:
            row.sort(reverse=True)
            for i in range(n):
                ans = max(ans, (i + 1) * row[i] )
        
        return ans

