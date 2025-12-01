class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        freq_element = [[freq, num] for num, freq in count.items()]

        minHeap = []

        for i in range(len(freq_element)):
            heapq.heappush(minHeap, [freq_element[i][0], freq_element[i][1]])

            if len(minHeap) > k:
                heapq.heappop(minHeap)
        

        return [ el for count, el in minHeap]