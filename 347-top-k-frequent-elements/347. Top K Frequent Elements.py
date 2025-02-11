class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        counts = [[val, key] for key, val in freq.items()]

        heap = []

        for i in range(len(counts)):
            heapq.heappush(heap, (counts[i][0], counts[i][1]))
            if len(heap) > k:
                heapq.heappop(heap)
        
        ans = []
        for c, v in heap:
            ans.append(v)
        
        return ans