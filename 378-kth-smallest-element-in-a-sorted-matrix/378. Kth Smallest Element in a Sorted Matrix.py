class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    
        pq = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                heapq.heappush(pq, -matrix[i][j])

                if len(pq) > k:
                    heapq.heappop(pq)
        
        return -pq[0]


    