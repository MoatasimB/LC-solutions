class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        minHeap = []
        curr = 0
        for num in nums:
            curr += num
            heapq.heappush(minHeap, num)
        

        count = 0
        while minHeap[0] < k and len(minHeap) >= 2:

            x = heapq.heappop(minHeap)
            y = heapq.heappop(minHeap)

            curr -= x
            curr -= y

            new = min(x,y)*2 + max(x,y)
            curr += new
            heapq.heappush(minHeap, new)
            count += 1
        

        return count if minHeap[0] >= k else 0
        
