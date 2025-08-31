class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        n = len(matrix)
        def find_counts(mid, smaller, larger):
            count = 0

            r = n - 1
            c = 0

            while r >= 0 and c <= n - 1:

                if matrix[r][c] > mid:
                    
                    larger = min(larger, matrix[r][c])
                    r -= 1
                else:
                    smaller = max(smaller, matrix[r][c])
                    count += r + 1
                    c += 1
            
            return count, smaller, larger
        

        l = matrix[0][0]
        r = matrix[n-1][n-1]
        

        while l < r:
            mid = (l + r) // 2
            smaller = matrix[0][0]
            larger = matrix[n-1][n-1]

            count, smaller, larger = find_counts(mid, smaller, larger)

            if count == k:
                return smaller
            elif count < k:
                l = larger
            else:
                r = smaller
        
        
        
        return l