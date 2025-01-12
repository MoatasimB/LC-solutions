class MedianFinder:

    def __init__(self):
        self.minH = [] #larger elements
        self.maxH = [] #Smaller elements 

    def addNum(self, num: int) -> None:
        
        heapq.heappush(self.maxH, -num)

        if len(self.maxH) > len(self.minH) + 1:
            element = -heapq.heappop(self.maxH)
            heapq.heappush(self.minH, element)
        
        if self.minH and self.maxH and -self.maxH[0] > self.minH[0]:
            element = -heapq.heappop(self.maxH)
            heapq.heappush(self.minH, element)

        if len(self.minH) > len(self.maxH) + 1:
            element = heapq.heappop(self.minH)
            heapq.heappush(self.maxH, -element)
        # print(self.maxH, self.minH)
    def findMedian(self) -> float:
        if len(self.minH) == len(self.maxH):
            return (self.minH[0] + (-self.maxH[0])) / 2
        
        elif len(self.minH) > len(self.maxH):
            return self.minH[0]
        
        else:
            return -self.maxH[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()