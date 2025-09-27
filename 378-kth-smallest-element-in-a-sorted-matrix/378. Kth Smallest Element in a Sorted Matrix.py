class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        n = len(matrix)
        
        h = []
        
        for i in range(n):
            heapq.heappush(h, [matrix[i][0], i, 0 ])
        
        ans = None
        while k:
            
            val, row, col = heapq.heappop(h)
            ans = val
            
            if col + 1 < n:
                heapq.heappush(h, [matrix[row][col + 1], row, col + 1])
                 
            k -= 1
        
        return ans
            