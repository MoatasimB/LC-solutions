class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        
        counts = [0] * 3
        total = [0] * 3

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                total[grid[i][j]] += 1

        n = len(grid)
        i = 0
        j = 0
        while i < n//2:
            counts[grid[i][j]] += 1
            total[grid[i][j]] -= 1
            i += 1
            j += 1
        i = 0
        j = n - 1
        while i < n//2:
            counts[grid[i][j]] += 1
            total[grid[i][j]] -= 1
            i += 1
            j -= 1

        i = n // 2
        j = n // 2

        while i < n:
            counts[grid[i][j]] += 1
            total[grid[i][j]] -= 1
            i += 1
        ans = float('inf')
        totalY = sum(counts)
        totalB = sum(total)
        for i in range(3):
            for j in range(3):
                if i!=j:
                    el_in_y_to_change = totalY - counts[i]
                    el_in_b_to_change = totalB - total[j]
                    ans = min(ans, el_in_y_to_change + el_in_b_to_change)
        return ans

        
       