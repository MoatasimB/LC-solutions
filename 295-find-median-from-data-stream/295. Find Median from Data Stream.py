class MedianFinder:

    def __init__(self):
        self.lower = [] #maxHeap
        self.higher = [] #minHeap
        
        # [1 3] [2]

    def addNum(self, num: int) -> None:

        heapq.heappush(self.lower, -num)

        if len(self.lower) > len(self.higher) + 1:
            num = -heapq.heappop(self.lower)
            heapq.heappush(self.higher, num)
        
        if self.lower and self.higher and -self.lower[0] > self.higher[0]:
            num = -heapq.heappop(self.lower)
            heapq.heappush(self.higher, num)
        
        if len(self.higher) > len(self.lower):
            num = heapq.heappop(self.higher)
            heapq.heappush(self.lower, - num)
        
        

    def findMedian(self) -> float:
        total = len(self.lower) + len(self.higher)

        if total % 2 == 0:
            return (self.higher[0] - self.lower[0]) / 2
        
        return -self.lower[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()