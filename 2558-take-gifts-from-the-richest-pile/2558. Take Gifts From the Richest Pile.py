class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        gifts =[-g for g in gifts]
        heapq.heapify(gifts)

        for _ in range(k):
            x = -1 * heapq.heappop(gifts)
            x = int(x**0.5)
            heapq.heappush(gifts, -x)
        
        return abs(sum(gifts))