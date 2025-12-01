class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x: x[0])
        minHeap = [] #endTime

        for i in range(len(intervals)):
            start, end = intervals[i]
            if minHeap and minHeap[0] <= start:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, end)
        
        return len(minHeap)