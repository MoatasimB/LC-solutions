class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distances = {}

        for i in range(len(points)):
            x, y  = points[i]
            distances[i] = x**2 + y**2
        

        max_heap = []

        for idx, dist in distances.items():

            heapq.heappush(max_heap, [-dist, idx])

            if len(max_heap) > k:
                heapq.heappop(max_heap)
        

        return [points[i] for _, i in max_heap]