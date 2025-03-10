class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, num)
        

        count = 0
        while minHeap[0] < k and len(minHeap) >= 2:

            x = heapq.heappop(minHeap)
            y = heapq.heappop(minHeap)

            new = min(x,y)*2 + max(x,y)
            heapq.heappush(minHeap, new)
            count += 1
        

        return count if minHeap[0] >= k else 0
        
