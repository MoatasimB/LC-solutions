class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        mpp = defaultdict(int)


        for num in nums:
            mpp[num] += 1
    
        min_heap = []

        for num, val in mpp.items():

            heapq.heappush(min_heap, [val, num])

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [num for _, num in min_heap]