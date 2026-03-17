class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0])
        heights = [[0] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 1:
                    heights[r][c] = 1 + (heights[r - 1][c] if r - 1 >= 0 else 0)
        
        ans = 0
        for row in heights:
            row.sort(reverse=True)
            currHeight = float("inf")
            for i in range(n):
                width = i + 1
                currHeight = min(currHeight, row[i])
                ans = max(ans, width * currHeight )
        
        return ans
