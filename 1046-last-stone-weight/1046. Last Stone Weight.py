class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        
        max_heap = [-s for s in stones]

        heapify(max_heap)

        while len(max_heap) > 1:
            first = -heapq.heappop(max_heap)
            second = -heapq.heappop(max_heap)

            if first == second:
                continue
            else:
                heapq.heappush(max_heap, -(first - second))
        
        if len(max_heap) == 0:
            return 0
        
        return -max_heap[0]