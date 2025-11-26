class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])

        def valid(row, col):
            return 0<=row<m and 0<=col<n

        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def dfs(row, col, effort):
            if (row, col) == (m-1, n-1):
                return True
            
            for dx, dy in directions:
                next_row = row + dx
                next_col = col + dy
                if valid(next_row, next_col) and (next_row, next_col) not in seen:
                    if abs(heights[row][col] - heights[next_row][next_col]) <= effort:
                        seen.add((next_row, next_col))
                        if dfs(next_row, next_col, effort):
                            return True
            return False
        
        left = 0
        right = max(max(row) for row in heights)

        while left<=right:
            mid = (left + right) // 2
            seen = {(0,0)}

            if dfs(0,0,mid):
                right = mid -1
            else:
                left = mid + 1
        
        return left
